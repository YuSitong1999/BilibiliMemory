import math

import dao
from api import Response, request_retry_json


class FavoriteResponse(Response):
    def __init__(self, resp: dict):
        super().__init__(resp)
        if self.code != 0:
            return
        self.title: str = resp['data']['info']['title']
        self.media_count: int = resp['data']['info']['media_count']

    def __str__(self):
        return f'收藏夹 {self.title} {self.media_count}'


def request_favorite(fid: int) -> FavoriteResponse:
    """
    获取收藏夹信息
    https://api.bilibili.com/x/v3/fav/resource/list?
        pn=1&ps=20&keyword=&order=mtime&type=0&tid=0&platform=web&jsonp=jsonp&
        media_id={fid}
    :param fid: 收藏夹id
    :return: 收藏夹信息
    """
    resp = request_retry_json(f'https://api.bilibili.com/x/v3/fav/resource/list?ps=1&media_id={fid}')
    return FavoriteResponse(resp)


class FavoriteContentMedia:
    def __init__(self, media: dict):
        self.id: int = media['id']
        self.title: str = media['title']
        self.cover: str = media['cover']
        self.intro: str = media['intro']
        self.page: int = media['page']
        self.duration: int = media['duration']
        self.upper_mid: int = media['upper']['mid']
        self.upper_name: str = media['upper']['name']
        self.ctime: int = media['ctime']
        self.pubtime: int = media['pubtime']
        self.fav_time: int = media['fav_time']
        self.bv_id: str = media['bv_id']
        self.first_cid: int = media['ugc']['first_cid']

    def __str__(self):
        return f'收藏投稿 {self.bv_id} {self.title} {self.upper_name}'


class FavoriteContentResponse(Response):
    def __init__(self, resp: dict):
        super().__init__(resp)
        if self.code != 0:
            return
        self.media_count: int = resp['data']['info']['media_count']
        self.medias: list[FavoriteContentMedia] = [FavoriteContentMedia(media) for media in resp['data']['medias']]

    def __str__(self):
        return f'收藏夹内容 {self.media_count}\n' + '\n'.join(['\t' + str(media) for media in self.medias])


def request_favorite_content(fid: int, page_number: int) -> FavoriteContentResponse:
    """
    获取收藏夹一页内容
    https://api.bilibili.com/x/v3/fav/resource/list?
        keyword=&order=mtime&type=0&tid=0&platform=web&jsonp=jsonp&ps=20&
        media_id={fid}&pn={page_number}
    :param fid: 收藏夹id
    :param page_number: 收藏夹中页码
    :return: 收藏夹一页内容
    """
    resp = request_retry_json(f'https://api.bilibili.com/x/v3/fav/resource/list?ps=20&media_id={fid}&pn={page_number}')
    return FavoriteContentResponse(resp)


def get_favorite_media_list(fid: int, limiters: list[dao.AimLimiter]) \
        -> tuple[FavoriteResponse, list[FavoriteContentMedia]]:
    """
    获取收藏夹至少符合一个限制条件的所有投稿
    :param fid: 收藏夹id
    :param limiters: 限制条件
    :return: 收藏夹信息, 收藏夹符合条件的所有投稿
    """
    # 收藏夹信息
    favorite_response = request_favorite(fid)
    if favorite_response.code != 0:
        print(favorite_response.message)
        return favorite_response, []

    # 最宽松的收藏时间限制
    loosest_after_limit: int | None = None
    for limiter in limiters:
        if limiter.after is None:
            loosest_after_limit = None
            break
        elif loosest_after_limit is None or limiter.after < loosest_after_limit:
            loosest_after_limit = limiter.after

    page_number: int = math.ceil(favorite_response.media_count / 20)
    media_list: list[FavoriteContentMedia] = []
    for i in range(1, page_number + 1):
        favorite_content_response = request_favorite_content(fid, i)
        if favorite_content_response.code != 0:
            return favorite_response, media_list
        for media in favorite_content_response.medias:
            if loosest_after_limit is not None and media.fav_time < loosest_after_limit:
                # 收藏时间早于最宽松的收藏时间限制，不再继续
                return favorite_response, media_list
            ok: bool = False
            for limiter in limiters:
                if (limiter.after is None or media.fav_time >= limiter.after) and \
                        (limiter.max_duration is None or media.duration <= limiter.max_duration):
                    ok = True
                    break
            if ok:
                media_list.append(media)
    return favorite_response, media_list
