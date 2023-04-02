import logging

import request


def generate_fav_url(fid: int) -> str:
    """
    获取收藏夹信息
    https://api.bilibili.com/x/v3/fav/resource/list?
        pn=1&ps=20&keyword=&order=mtime&type=0&tid=0&platform=web&jsonp=jsonp&
        media_id={fid}
    :param fid: 收藏夹id
    :return: 获取收藏夹信息url
    """
    return f'https://api.bilibili.com/x/v3/fav/resource/list?ps=1&media_id={fid}'


def generate_fav_content_url(fid: int, page_number: int) -> str:
    """
    获取收藏夹一页内容
    https://api.bilibili.com/x/v3/fav/resource/list?
        keyword=&order=mtime&type=0&tid=0&platform=web&jsonp=jsonp&ps=20&
        media_id={fid}&pn={page_number}
    :param fid: 收藏夹id
    :param page_number: 收藏夹中页码
    :return: 获取收藏夹一页内容url
    """
    return f'https://api.bilibili.com/x/v3/fav/resource/list?ps=20&media_id={fid}&pn={page_number}'


def generate_user_detail_url(mid: int) -> str:
    """
    获取用户信息
    https://api.bilibili.com/x/space/acc/info?
        mid={用户ID}
    :param mid: UP主id
    :return:
    """
    return f"https://api.bilibili.com/x/space/acc/info?mid={mid}"


def generate_upper_content_url(mid: int, page_number: int) -> str:
    """
    获取UP主投稿一页内容
    https://api.bilibili.com/x/space/arc/search?ps=50&
        mid={UP主ID}&pn={页码，从1开始}
    :param mid: UP主id
    :param page_number: 收藏夹中页码
    :return: 获取收藏夹一页内容url
    """
    return f'https://api.bilibili.com/x/space/arc/search?ps=50&mid={mid}&pn={page_number}'


def generate_media_detail_url(bv_id: str) -> str:
    """
    获取投稿信息
    https://api.bilibili.com/x/web-interface/view/detail?
        bvid={bv——id}
    :param bv_id: 投稿bv号
    :return: 获取投稿信息url
    """
    return f'https://api.bilibili.com/x/web-interface/view/detail?bvid={bv_id}'


def generate_media_pages_url(bv_id: str) -> str:
    """
    获取投稿所有分P信息
    https://api.bilibili.com/x/player/pagelist?jsonp=jsonp&
        bvid={bv_id}
    :param bv_id: 投稿bv号
    :return: 所有分P信息url
    """
    return f'https://api.bilibili.com/x/player/pagelist?bvid={bv_id}'


def generate_media_audio_video_url(bv_id: str, cid: int) -> [list[str], list[str]]:
    """
    获取投稿的音频、视频URL
    https://api.bilibili.com/x/player/playurl?qn=120&type=&otype=json&fourk=1&fnver=0&fnval=976&
        bvid={bv_id}&cid={cid}
    :param bv_id: bv号
    :param cid: 分P id
    :return: 音频、视频URL
    """
    logging.info(f'get media url {bv_id} {cid} :')
    url = f'https://api.bilibili.com/x/player/playurl?fnval=976&bvid={bv_id}&cid={cid}'
    resp = request.request_retry_json(url)
    media_info = resp['data']['dash']
    audio_url_list: list[str] = [media_info['audio'][0]['base_url'], ] + media_info['audio'][0]['backup_url']
    video_url_list: list[str] = [media_info['video'][0]['base_url'], ] + media_info['video'][0]['backup_url']
    logging.info(f'get media url {bv_id} {cid} finished.')
    return [audio_url_list, video_url_list]
