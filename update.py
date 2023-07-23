import logging
import math
import time

import api
import bvid_aid
import config
import dao
from aim import AIM_FAVORITE_TYPE_ID, AIM_MEDIA_TYPE_ID, AIM_UPPER_TYPE_ID


def generate_update_timestamp() -> int:
    return math.floor(time.time())


# def generate_html(local_bv_id_set: set[str]):
#     # 读取所有本地投稿信息
#     media_list: list[dict] = []
#     for bv_id in local_bv_id_set:
#         # 读投稿数据
#         media = file.read_media_json(bv_id)
#         media_list.append(media)
#
#     # 按收藏时间（如果有）或发布时间排序
#     media_list.sort(key=lambda m: str(m.get('fav_time', m.get('created', ''))), reverse=True)
#     # 生成网页
#     html_content: str = ''
#     for media in media_list:
#         # FIXME 投稿信息格式不统一
#         author = media.get('author', '')
#         if author == '':
#             author = media.get('upper', None)
#             if author is not None:
#                 author = author['name']
#         html_content += f'''
#     <tr>
#         <td><img src="../all/{media['bv_id']}.jpg" alt="封面图片" style="height: 100px"/></td>
#         <td>{media['title']}</td>
#         <td>{author}</td>
#         <td>{timestamp_to_time(media.get('pubtime', media.get('created', '')))}</td>
#         <td>{timestamp_to_time(media.get('fav_time', ''))}</td>
#         <td>{media['duration'] // 3600}:{media['duration'] // 60 % 60}:{media['duration'] % 60}</td>
#         <td><a href="../all/{media['bv_id']}.mp4" target="_blank">本地视频</a></td>
#         <td>{media.get('intro', '')}</td>
#     </tr>'''
#
#     # 写网页文件
#     file.write_html(html_content)


def download_media(bv_id: str, cid: int, page_count: int) -> bool:
    api.download_media(bv_id, cid, config.all_media_path, 1)
    if page_count > 1:
        pages_response = api.request_media_pages(bv_id)
        if pages_response.code != 0:
            logging.error(f'获取投稿分P失败: {bv_id}')
            return False
        for page_id in range(1, page_count + 1):
            api.download_media(bv_id, pages_response.pages[page_id].cid,
                               config.all_media_path, page_id)
    return True


def main():
    """
    执行更新备份
    :return: None
    """

    # 整理本地信息
    local_media_list = dao.get_all_media()

    # 本地所有备份的bv号：本地已备份，（上次获取时）线上未被删
    local_exists_bv_id_set: set[str] = set(
        [media.bv_id for media in local_media_list if media.is_local and not media.is_delete])
    # 已被删除备份的bv号：本地已备份，（上次获取时）线上已被删
    local_deleted_bv_id_set: set[str] = set(
        [media.bv_id for media in local_media_list if media.is_local and media.is_delete])
    # 未及时备份被删投稿的残余信息和bv号：本地未备份
    local_lost_bv_id_set: set[str] = set(
        [media.bv_id for media in local_media_list if not media.is_local])

    aim_list = dao.get_all_aim()
    for aim in aim_list:
        # 限制
        limiters = dao.get_aim_limiter_by_aim_id(aim.id)

        if aim.type == AIM_FAVORITE_TYPE_ID:
            logging.info(f'更新收藏夹: {aim.target_id} {aim.name}')
            # 获取收藏夹及投稿信息
            favorite_response, now_online_media_list = api.get_favorite_media_list(aim.target_id, limiters)

            # 更新收藏夹信息
            dao.update_aim_by_id(aim.id, favorite_response.title, generate_update_timestamp())

            for media in now_online_media_list:
                # 获取和更新UP主信息
                upper_response = api.upper.request_user_detail(media.upper_mid)
                if upper_response.code != 0:
                    logging.error(f'获取UP主失败: {media.upper_mid} {media.upper_name}')
                else:
                    dao.save_upper(upper_response.mid, upper_response.name, upper_response.sign,
                                   generate_update_timestamp())

                # 更新投稿信息
                if media.bv_id in local_exists_bv_id_set:  # 本地已存在
                    if media.title == '已失效视频':  # 本地已存在，线上已被删除
                        # 线上已被删除,更新投稿信息
                        dao.update_media_status(media.bv_id, True, True)
                        # 更新本地状态
                        local_exists_bv_id_set.discard(media.bv_id)
                        local_deleted_bv_id_set.add(media.bv_id)
                    else:  # 本地已存在，线上有效
                        # TODO 检查是否有更新
                        # 更新投稿信息
                        dao.update_media_status(media.bv_id, True, False)
                elif media.bv_id in local_deleted_bv_id_set:  # 本地被标记为删除
                    if media.title == '已失效视频':  # 本地被标记为删除，线上已被删除
                        # 更新投稿信息
                        dao.update_media_status(media.bv_id, True, True)
                    else:  # 本地被标记为删除，线上已恢复
                        # 更新投稿信息
                        dao.update_media_status(media.bv_id, True, False)
                        # 更新本地状态
                        local_exists_bv_id_set.add(media.bv_id)
                        local_deleted_bv_id_set.discard(media.bv_id)
                else:  # 本地不存在
                    if media.title == '已失效视频':  # 本地不存在，线上已被删除
                        # 记录残余信息
                        dao.insert_or_replace_media(media.bv_id, media.upper_mid, media.title, media.intro,
                                                    media.duration, media.ctime, media.fav_time,
                                                    generate_update_timestamp(), False, True)
                        # 更新本地状态
                        local_lost_bv_id_set.add(media.bv_id)
                    else:  # 本地不存在，线上有效
                        # 下载视频
                        if not download_media(media.bv_id, media.first_cid, media.page):
                            continue
                        # 更新投稿信息
                        dao.insert_or_replace_media(media.bv_id, media.upper_mid, media.title, media.intro,
                                                    media.duration, media.ctime, media.fav_time,
                                                    generate_update_timestamp(), True, False)
                        # 更新本地状态
                        local_exists_bv_id_set.add(media.bv_id)

                # 更新投稿所属目标
                dao.save_media_aim(media.bv_id, aim.id)
                # end for media in now_online_media_list
            # end if aim.type == AIM_FAVORITE_TYPE_ID
        elif aim.type == AIM_UPPER_TYPE_ID:
            logging.info(f'更新UP主: {aim.target_id} {aim.name}')
            # 获取Up主及投稿信息
            upper_response, now_online_media_list = api.get_upper_media_list(aim.target_id, limiters)

            # 更新UP主信息
            dao.save_upper(aim.target_id, upper_response.name, upper_response.sign, generate_update_timestamp())

            # 更新UP主投稿信息
            for media in now_online_media_list:
                # 更新投稿信息
                if media.bv_id in local_exists_bv_id_set:  # 本地已存在
                    # 更新投稿信息
                    dao.update_media_status(media.bv_id, True, False)
                elif media.bv_id in local_deleted_bv_id_set:  # 本地标记为删除
                    # 更新投稿信息
                    dao.update_media_status(media.bv_id, True, False)
                    # 更新本地状态
                    local_exists_bv_id_set.add(media.bv_id)
                    local_deleted_bv_id_set.discard(media.bv_id)
                else:  # 本地不存在
                    # 获取投稿信息
                    media_detail = api.request_media_detail(media.bv_id)
                    # 下载视频
                    if not download_media(media_detail.bv_id, media_detail.pages_cid_list[0],
                                          len(media_detail.pages_cid_list)):
                        continue
                    # 更新投稿信息
                    dao.insert_or_replace_media(media_detail.bv_id, media_detail.owner_id, media_detail.title,
                                                media_detail.desc, media_detail.duration, media_detail.ctime,
                                                media_detail.ctime, generate_update_timestamp(), True, False)
                    # 更新本地状态
                    local_exists_bv_id_set.add(media_detail.bv_id)

                # 更新投稿所属目标
                dao.save_media_aim(media.bv_id, aim.id)
                # end for media in now_online_media_list
            # end elif aim.type == AIM_UPPER_TYPE_ID
        elif aim.type == AIM_MEDIA_TYPE_ID:
            logging.info(f'更新投稿: {aim.target_id} {aim.name}')
            # 获取投稿信息
            bv_id = bvid_aid.aid_to_bv_id(aim.target_id)
            media = api.request_media_detail(bv_id)

            if media.code != 0 and media.code != -404:
                logging.error(f'获取投稿失败: {aim.target_id} {bv_id} : {media.code} {media.message}')
                continue

            # 获取和更新UP主信息
            upper_response = api.upper.request_user_detail(media.owner_id)
            if upper_response.code != 0:
                logging.error(f'获取UP主失败: {media.owner_id} {media.title}')
            else:
                dao.save_upper(upper_response.mid, upper_response.name, upper_response.sign,
                               generate_update_timestamp())

            if bv_id in local_exists_bv_id_set:  # 本地已存在
                if media.code == -404:  # 本地已存在，线上已被删除
                    # 线上已被删除,更新投稿信息
                    dao.update_media_status(media.bv_id, True, True)
                    # 更新本地状态
                    local_exists_bv_id_set.discard(bv_id)
                    local_deleted_bv_id_set.add(bv_id)
                else:  # 本地已存在，线上有效
                    # TODO 检查是否有更新
                    # 更新投稿信息
                    dao.update_media_status(media.bv_id, True, False)
            elif bv_id in local_deleted_bv_id_set:  # 本地被标记为删除
                if media.code == -404:  # 本地被标记为删除，线上已被删除
                    # 更新投稿信息
                    dao.update_media_status(media.bv_id, True, True)
                else:  # 本地被标记为删除，线上已恢复
                    # 更新投稿信息
                    dao.update_media_status(media.bv_id, True, False)
                    # 更新本地状态
                    local_exists_bv_id_set.add(bv_id)
                    local_deleted_bv_id_set.discard(bv_id)
            else:  # 本地不存在
                if media.code == -404:  # 本地不存在，无残留信息可供保留
                    pass
                else:
                    # 下载视频
                    if not download_media(media.bv_id, media.pages_cid_list[0], len(media.pages_cid_list)):
                        continue
                    # 更新投稿信息
                    dao.insert_or_replace_media(media.bv_id, media.owner_id, media.title, media.desc,
                                                media.duration, media.ctime, media.ctime,
                                                generate_update_timestamp(), True, False)
                    # 更新本地状态
                    local_exists_bv_id_set.add(media.bv_id)

            # 更新投稿所属目标
            dao.save_media_aim(media.bv_id, aim.id)
            # end elif aim.type == AIM_MEDIA_TYPE_ID
        else:
            logging.error(f'未知备份目标类型: {aim.type}')
            continue

    # 输出丢失投稿的 bv_id
    for bv_id in local_lost_bv_id_set:
        logging.warning(f'丢失投稿: {bv_id}')
