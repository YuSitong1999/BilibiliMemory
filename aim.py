import getopt
import logging
import math
import sys
import time

import api
import bvid_aid
import dao

AIM_FAVORITE_TYPE_ID = 0
AIM_MEDIA_TYPE_ID = 1
AIM_UPPER_TYPE_ID = 2

command_aim = '''
    python main.py aim
        status
        add <收藏夹ID1>[,<收藏夹ID2>,...,<收藏夹IDN>] [-a <最早发布时间>] [-d <投稿时长秒数>]
        addm <投稿BV ID1>[,...,<投稿BV IDN>]
        addu <UP主 ID1>[,...,<UP主 IDN>] [-a <最早发布时间>] [-d <投稿时长秒数>]
        rm <备份目标ID1>[,...,<备份目标IDN>]
        rml <备份目标限制条件ID1>[,...,<备份目标限制条件IDN>]
    '''


def aim_add_media(argv: list[str]) -> None:
    """
    新增备份目标投稿
    :param argv: <投稿BV ID1>[,...,<投稿BV IDN>]
    """
    if len(argv) < 1:
        logging.error(f'参数个数错误!\n{command_aim}')
        return

    for bv_id in argv[0].split(','):
        # bvid to aid
        aid = bvid_aid.bv_id_to_aid(bv_id)
        # 投稿可能已抓取
        media = dao.get_media_by_bv_id(bv_id)
        name: str
        if media is None:
            # 获取投稿信息
            media_response = api.media.request_media_detail(bv_id)
            name = media_response.title
        else:
            name = media.title
        # 加入记录
        dao.insert_or_replace_aim(AIM_MEDIA_TYPE_ID, aid, name)


def parse_argv(argv: list[str]) -> tuple[int, int]:
    """
    解析参数
    :param argv: 参数
    :return: after_timestamp, max_duration
    """
    try:
        opts, args = getopt.getopt(argv, "a:d:", [])
    except getopt.GetoptError:
        logging.error(f'参数错误{command_aim}')
        sys.exit(1)

    after_timestamp: int | None = None
    max_duration: int | None = None
    for opt, arg in opts:
        if opt == '-a':
            after_timestamp = math.floor(time.mktime(time.strptime(arg, '%Y-%m-%d')))
        elif opt == '-d':
            max_duration = int(arg)
    return after_timestamp, max_duration


def aim_add_favorites(argv: list[str]) -> None:
    """
    新增备份目标收藏夹
    :param argv: <收藏夹ID1>[,<收藏夹ID2>,...,<收藏夹IDN>] [-a <最早发布时间>] [-d <投稿时长秒数>]
    """
    if len(argv) < 1:
        logging.error(f'参数个数错误!\n{command_aim}')
        sys.exit(1)

    after_timestamp, max_duration = parse_argv(argv[1:])

    for s in argv[0].split(','):
        if not s.isnumeric():
            logging.error(f'参数{s}错误,已跳过')
            continue
        fid: int = int(s)
        # 获取相同目标收藏
        aim_favorite: dao.Aim | None = dao.get_aim_by_type_and_target_id(AIM_FAVORITE_TYPE_ID, fid)
        if aim_favorite is None:
            # 获取收藏夹信息
            favorite_response = api.favorite.request_favorite(fid)
            dao.insert_or_replace_aim(AIM_FAVORITE_TYPE_ID, fid, favorite_response.title)
            aim_favorite = dao.get_aim_by_type_and_target_id(AIM_FAVORITE_TYPE_ID, fid)

        # 加入新目标限制
        dao.insert_aim_limiter(aim_favorite.id, after_timestamp, max_duration)


def aim_add_uppers(argv: list[str]):
    """
    新增备份目标UP主
    :param argv: <UP主 ID1>[,...,<UP主 IDN>] [-a <最早发布时间>] [-d <投稿时长秒数>]
    """
    if len(argv) < 1:
        logging.error(f'参数个数错误!\n{command_aim}')
        sys.exit(1)

    after_timestamp, max_duration = parse_argv(argv[1:])

    for s in argv[0].split(','):
        if not s.isnumeric():
            logging.error(f'参数{s}错误,已跳过')
            continue
        mid = int(s)
        # 获取相同目标Up主
        aim_upper: dao.Aim | None = dao.get_aim_by_type_and_target_id(AIM_UPPER_TYPE_ID, mid)
        if aim_upper is None:
            # 获取Up主信息
            upper_response = api.upper.request_user_detail(mid)
            dao.insert_or_replace_aim(AIM_UPPER_TYPE_ID, mid, upper_response.name)
            aim_upper = dao.get_aim_by_type_and_target_id(AIM_UPPER_TYPE_ID, mid)

        # 加入新目标限制
        dao.insert_aim_limiter(aim_upper.id, after_timestamp, max_duration)


def rm_aim(argv: list[str]) -> None:
    """
    删除备份目标
    :param argv: <备份目标ID1>[,...,<备份目标IDN>]
    """
    if len(argv) != 1:
        logging.error(f'参数个数错误!\n{command_aim}')
        return

    for s in argv[0].split(','):
        if not s.isnumeric():
            logging.error(f'参数{s}错误,已跳过')
            continue
        aim_id = int(s)
        dao.delete_aim_by_id(aim_id)


def rm_aim_limiter(argv: list[str]) -> None:
    """
    删除备份目标限制条件

    :param argv: <备份目标限制条件ID1>[,...,<备份目标限制条件IDN>]
    """
    if len(argv) != 1:
        logging.error(f'参数个数错误!\n{command_aim}')
        return

    for s in argv[0].split(','):
        if not s.isnumeric():
            logging.error(f'参数{s}错误,已跳过')
            continue
        aim_limiter_id = int(s)
        dao.delete_aim_limiter_by_id(aim_limiter_id)


def main(argv: list[str]):
    """
    备份目标
    :param argv:
    :return:
    """

    operation_status = 'status'
    operation_add_favorites = 'add'
    operation_add_media = 'addm'
    operation_add_upper = 'addu'
    operation_rm = 'rm'
    operation_rm_limiter = 'rml'

    operations = (operation_status, operation_add_favorites,
                  operation_add_media, operation_add_upper, operation_rm)
    if len(argv) == 0 or argv[0] not in operations:
        logging.error(f'命令"{argv}"不受支持，请输入支持的命令:\n{command_aim}')
        return

    operation = argv[0]
    argv = argv[1:]

    if operation == operation_add_favorites:
        # 新增备份目标收藏夹
        aim_add_favorites(argv)
    elif operation == operation_add_upper:
        # 新增目标UP主
        aim_add_uppers(argv)
        pass
    elif operation == operation_add_media:
        # 新增备份目标投稿
        aim_add_media(argv)
    elif operation == operation_rm:
        # 删除备份目标
        rm_aim(argv)
    elif operation == operation_rm_limiter:
        # 删除备份目标限制条件
        rm_aim_limiter(argv)
    else:
        aim_list = dao.get_all_aim()
        aim_favorites = [aim for aim in aim_list if aim.type == AIM_FAVORITE_TYPE_ID]
        aim_uppers = [aim for aim in aim_list if aim.type == AIM_UPPER_TYPE_ID]
        aim_medias = [aim for aim in aim_list if aim.type == AIM_MEDIA_TYPE_ID]

        # 查看当前备份目标收藏夹
        aim_favorites_len = len(aim_favorites)
        logging.info(f'当前备份目标收藏夹: {aim_favorites_len}')
        if aim_favorites_len == 0:
            logging.info('查看当前目标收藏夹为空!')
        for aim in aim_favorites:
            logging.info(aim)
            aim_limiter_list = dao.get_aim_limiter_by_aim_id(aim.id)
            for aim_limiter in aim_limiter_list:
                logging.info(f'\t{aim_limiter}')
        logging.info('')

        # 查看当前备份目标UP主
        aim_uppers_len = len(aim_uppers)
        logging.info(f'当前备份目标UP主:{aim_uppers_len}')
        if aim_uppers_len == 0:
            logging.info('查看当前目标UP主为空!')
        for aim in aim_uppers:
            logging.info(aim)
            aim_limiter_list = dao.get_aim_limiter_by_aim_id(aim.id)
            for aim_limiter in aim_limiter_list:
                logging.info(f'\t{aim_limiter}')
        logging.info('')

        # 查看当前备份目标投稿
        aim_medias_len = len(aim_medias)
        logging.info(f'当前备份目标投稿: {aim_medias_len}', )
        if aim_medias_len == 0:
            logging.info('查看当前目标投稿为空!')
        for aim in aim_medias:
            logging.info(aim)
            aim_limiter_list = dao.get_aim_limiter_by_aim_id(aim.id)
            for aim_limiter in aim_limiter_list:
                logging.info(f'\t{aim_limiter}')
        logging.info('')
