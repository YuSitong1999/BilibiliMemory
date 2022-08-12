import logging
import os

import file
import request


def get_media_url(bv_id: str, first_cid: int) -> [str, str]:
    """
    获取投稿的音频、视频URL
    :param bv_id: bv号
    :param first_cid: 首P id
    :return: 音频、视频URL
    """
    logging.info('get media url ' + bv_id + ' ' + str(first_cid) + ' :')
    url = 'https://api.bilibili.com/x/player/playurl?qn=120&type=&otype=json&fourk=1&fnver=0&fnval=976&bvid=%s&cid=%d' \
          % (bv_id, first_cid)
    resp = request.request_retry_json(url)
    media_info = resp['data']['dash']
    audio_url = media_info['audio'][0]['base_url']
    video_url = media_info['video'][0]['base_url']
    logging.info('get media url ' + bv_id + ' ' + str(first_cid) + ' finished.')
    return audio_url, video_url


def download_file(bv_id: str, url: str, file_path: str):
    fake_referer_url = 'https://www.bilibili.com/video/' + bv_id
    resp = request.request_retry(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55',
        'referer': fake_referer_url,
        'range': 'bytes=0-'})
    with open(file_path, 'wb') as file:
        file.write(resp.content)


def merge_media(audio_file_path: str, video_file_path: str, file_path: str):
    rst = os.system(
        'ffmpeg-n5.0-latest-win64-lgpl-shared-5.0\\bin\\ffmpeg -i %s -i %s'
        ' -c:v copy -c:a aac -strict experimental %s' % (video_file_path, audio_file_path, file_path))
    if rst != 0:
        raise 'ffmpeg error'
    os.remove(audio_file_path)
    os.remove(video_file_path)


def download_media(bv_id: str, first_cid: int, media_path: str, page_id: str):
    audio_url, video_url = get_media_url(bv_id, first_cid)
    # 下载音频
    audio_file_path = os.path.join(file.tmp_path, 'tmp_audio.m4s')
    logging.info('download audio ' + bv_id + ' ' + str(first_cid) + ':')
    download_file(bv_id, audio_url, audio_file_path)
    logging.info('download audio ' + bv_id + ' ' + str(first_cid) + ' finished.')
    # 下载视频
    video_file_path = os.path.join(file.tmp_path, 'tmp_video.m4s')
    logging.info('download video ' + bv_id + ' ' + str(first_cid) + ':')
    download_file(bv_id, video_url, video_file_path)
    logging.info('download video ' + bv_id + ' ' + str(first_cid) + ' finished.')
    # 合并音视频后删除临时文件
    if page_id != '':
        file_path = os.path.join(media_path, bv_id + '_' + page_id + '.mp4')
    else:
        file_path = os.path.join(media_path, bv_id + '.mp4')
    logging.info('merge media ' + bv_id + ' ' + str(first_cid))
    merge_media(audio_file_path, video_file_path, file_path)
