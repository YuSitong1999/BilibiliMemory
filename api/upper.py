import logging
import math

import dao
from api import Response, request_retry_json

import api.wbi as wbi


class UpperDetailResponse(Response):
    def __init__(self, resp: dict):
        super().__init__(resp)
        if self.code != 0:
            return
        self.mid: int = resp['data']['mid']
        self.name: str = resp['data']['name']
        self.sign: str = resp['data']['sign']

    def __str__(self):
        if self.code != 0:
            return f'UP主 {self.code} {self.message}'
        return f'UP主 {self.mid} {self.name} {self.sign}'


def request_user_detail(mid: int) -> UpperDetailResponse:
    """
    获取用户信息
    https://api.bilibili.com/x/space/acc/info?
        mid={用户ID}
    :param mid: UP主id
    :return: 获取用户信息
    """
    resp = request_retry_json(f"https://api.bilibili.com/x/space/wbi/acc/info?{wbi.get_query(mid=mid)}")
    return UpperDetailResponse(resp)


class UpperContentMedia:
    def __init__(self, media: dict):
        self.title: str = media['title']
        self.created: int = media['created']
        self.length: str = media['length']
        self.aid: int = media['aid']
        self.bv_id: str = media['bvid']

    def __str__(self):
        return f'UP主投稿 {self.bv_id} {self.title} {self.created} {self.length}'


class UpperContentResponse(Response):
    def __init__(self, resp: dict):
        super().__init__(resp)
        if self.code != 0:
            return
        self.media_count: int = resp['data']['page']['count']
        self.medias: list[UpperContentMedia] = [UpperContentMedia(media) for media in resp['data']['list']['vlist']]

    def __str__(self):
        if self.code != 0:
            return f'UP主一页投稿 {self.code} {self.message}'
        return f'UP主一页投稿 {self.media_count} {len(self.medias)}\n' + '\n'.join(
            ['\t' + str(media) for media in self.medias])


def request_upper_content(mid: int, page_number: int) -> UpperContentResponse:
    """
    获取UP主投稿一页内容
    https://api.bilibili.com/x/space/arc/search?ps=50&
        mid={UP主ID}&pn={页码，从1开始}
    :param mid: UP主id
    :param page_number: 收藏夹中页码
    :return: UP主投稿一页内容
    """
    resp = request_retry_json(f'https://api.bilibili.com/x/space/wbi/arc/search?'
                              f'{wbi.get_query(ps=50, mid=mid, pn=page_number)}')
    return UpperContentResponse(resp)


def get_upper_media_list(mid: int, limiters: list[dao.AimLimiter]) \
        -> tuple[UpperDetailResponse, list[UpperContentMedia]]:
    """
    获取UP主的所有投稿信息
    :param mid: up主id
    :return: UP主信息和线上所有投稿信息
    """
    # 获取UP主信息
    detail_resp = request_user_detail(mid)
    if detail_resp.code != 0:
        logging.error(f'获取UP主信息失败: {mid}')
        return detail_resp, []

    # 最宽松的收藏时间限制
    loosest_after_limit: int | None = None
    for limiter in limiters:
        if limiter.after is None:
            loosest_after_limit = None
            break
        elif loosest_after_limit is None or limiter.after < loosest_after_limit:
            loosest_after_limit = limiter.after

    # 获取第一页后才知道页数
    page_number: int = 1
    media_list: list[UpperContentMedia] = []
    page_id: int = 1
    while page_id <= page_number:
        upper_content_response = request_upper_content(mid, page_id)
        if upper_content_response.code != 0:
            logging.error(f'获取UP主投稿失败: {mid}')
            return detail_resp, media_list
        page_number = math.ceil(upper_content_response.media_count / 50)
        for media in upper_content_response.medias:
            if loosest_after_limit is not None and media.created < loosest_after_limit:
                # 收藏时间早于最宽松的收藏时间限制，不再继续
                return detail_resp, media_list
            # 解析时长 格式为([0-9]+\:)?[0-9]{2}\:[0-9]{2}
            length: int = 0
            for s in media.length.split(':'):
                length *= 60
                length += int(s)
            ok: bool = False
            for limiter in limiters:
                if (limiter.after is None or media.created >= limiter.after) and \
                        (limiter.max_duration is None or length <= limiter.max_duration):
                    ok = True
                    break
            if ok:
                media_list.append(media)
        media_list.extend(upper_content_response.medias)
        page_id += 1

    return detail_resp, media_list
