import logging
import os

import api
import config
import file
from api import Response, request_retry_json


class MediaDetailResponse(Response):
    def __init__(self, resp: dict):
        super().__init__(resp)
        if self.code != 0:
            return
        self.bv_id: str = resp['data']['View']['bvid']
        self.aid: int = resp['data']['View']['aid']
        self.videos: int = resp['data']['View']['videos']
        self.pic: str = resp['data']['View']['pic']
        self.title: str = resp['data']['View']['title']
        self.pubdate: int = resp['data']['View']['pubdate']
        self.ctime: int = resp['data']['View']['ctime']
        self.desc: str = resp['data']['View']['desc']
        self.duration: int = resp['data']['View']['duration']
        self.owner_id: int = resp['data']['View']['owner']['mid']
        self.pages_cid_list: list[int] = [page['cid'] for page in resp['data']['View']['pages']]

    def __str__(self):
        return f'投稿 {self.bv_id} {self.title} {self.owner_id} {self.pages_cid_list}'


def request_media_detail(bv_id: str) -> MediaDetailResponse:
    """
    获取投稿信息
    https://api.bilibili.com/x/web-interface/view/detail?
        bvid={bv——id}
    :param bv_id: 投稿bv号
    :return: 投稿信息
    """
    resp = request_retry_json(f'https://api.bilibili.com/x/web-interface/view/detail?bvid={bv_id}')
    return MediaDetailResponse(resp)


class MediaPage:
    def __init__(self, page: dict):
        self.cid: int = page['cid']
        self.part: str = page['part']
        self.duration: int = page['duration']
        self.first_frame: str = page['first_frame']

    def __str__(self):
        return f'投稿分P {self.cid} {self.part} {self.duration}'


class MediaPagesResponse(Response):
    def __init__(self, resp: dict):
        super().__init__(resp)
        if self.code != 0:
            return
        self.pages: list[MediaPage] = [MediaPage(page) for page in resp['data']]

    def __str__(self):
        return f'投稿分P {len(self.pages)}\n' + '\n'.join(['\t' + str(page) for page in self.pages])


def request_media_pages(bv_id: str) -> MediaPagesResponse:
    """
    获取投稿所有分P信息
    https://api.bilibili.com/x/player/pagelist?jsonp=jsonp&
        bvid={bv_id}
    :param bv_id: 投稿bv号
    :return: 投稿所有分P信息
    """
    resp = request_retry_json(f'https://api.bilibili.com/x/player/pagelist?bvid={bv_id}')
    return MediaPagesResponse(resp)


def request_media_audio_video(bv_id: str, cid: int) -> tuple[list[str], list[str]]:
    """
    获取投稿的音频、视频
    https://api.bilibili.com/x/player/playurl?qn=120&type=&otype=json&fourk=1&fnver=0&fnval=976&
        bvid={bv_id}&cid={cid}
    :param bv_id: bv号
    :param cid: 分P id
    :return: 音频、视频URL
    """
    logging.info(f'get media url {bv_id} {cid} :')
    resp = request_retry_json(f'https://api.bilibili.com/x/player/playurl?fnval=976&bvid={bv_id}&cid={cid}')
    media_info = resp['data']['dash']
    audio_url_list: list[str] = [media_info['audio'][0]['base_url'], ] + media_info['audio'][0]['backup_url']
    video_url_list: list[str] = [media_info['video'][0]['base_url'], ] + media_info['video'][0]['backup_url']
    logging.info(f'get media url {bv_id} {cid} finished.')
    return audio_url_list, video_url_list


def download_file_url_list(bv_id: str, url_list: list[str], file_path: str):
    fake_referer_url = 'https://www.bilibili.com/video/' + bv_id
    resp = api.request_retry_url_list(url_list, headers={
        'referer': fake_referer_url,
        'range': 'bytes=0-'})
    with open(file_path, 'wb') as f:
        f.write(resp.content)


def download_file(bv_id: str, url: str, file_path: str):
    fake_referer_url = 'https://www.bilibili.com/video/' + bv_id
    resp = api.request_retry(url, headers={
        'referer': fake_referer_url,
        'range': 'bytes=0-'})
    with open(file_path, 'wb') as f:
        f.write(resp.content)


def merge_media(audio_file_path: str, video_file_path: str, file_path: str):
    rst = os.system(
        'ffmpeg-n5.0-latest-win64-lgpl-shared-5.0\\bin\\ffmpeg -i %s -i %s'
        ' -c:v copy -c:a aac -strict experimental %s' % (video_file_path, audio_file_path, file_path))
    if rst != 0:
        raise 'ffmpeg error'
    os.remove(audio_file_path)
    os.remove(video_file_path)


def download_media(bv_id: str, first_cid: int, media_path: str, page_id: int):
    audio_url_list, video_url_list = request_media_audio_video(bv_id, first_cid)
    # 下载音频
    audio_file_path = os.path.join(media_path, 'tmp_audio.m4s')
    logging.info('download audio ' + bv_id + ' ' + str(first_cid) + ':')
    download_file_url_list(bv_id, audio_url_list, audio_file_path)
    logging.info('download audio ' + bv_id + ' ' + str(first_cid) + ' finished.')
    # 下载视频
    video_file_path = os.path.join(media_path, 'tmp_video.m4s')
    logging.info('download video ' + bv_id + ' ' + str(first_cid) + ':')
    download_file_url_list(bv_id, video_url_list, video_file_path)
    logging.info('download video ' + bv_id + ' ' + str(first_cid) + ' finished.')
    # 合并音视频后删除临时文件
    file_path = os.path.join(media_path, bv_id + '_' + str(page_id) + '.mp4')
    logging.info('merge media ' + bv_id + ' ' + str(first_cid))
    merge_media(audio_file_path, video_file_path, file_path)


def check_online_available(bv_id: str) -> bool:
    """
    检查投稿是否可用

    :param bv_id: 投稿bv号
    :return: 是否可用
    """
    resp = request_media_pages(bv_id)
    return resp.code == 0
