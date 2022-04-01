import requests
import json
import os


def get_media_url(bv_id: str, first_cid: int) -> [str, str]:
    url = 'https://api.bilibili.com/x/player/playurl?qn=120&type=&otype=json&fourk=1&fnver=0&fnval=976&bvid=%s&cid=%d' \
          % (bv_id, first_cid)
    print(url)
    req = requests.get(url)
    media_info = json.loads(req.text)['data']['dash']
    audio_url = media_info['audio'][0]['base_url']  # TODO baseUrl?
    video_url = media_info['video'][0]['base_url']
    return audio_url, video_url


def download_file(bv_id: str, url: str, file_path: str):
    fake_referer_url = 'https://www.bilibili.com/video/' + bv_id
    req = requests.get(url, headers={'User-Agent': 'PostmanRuntime/7.28.4', 'referer': fake_referer_url,
                                     'range': 'bytes=0-'})
    with open(file_path, 'wb') as file:
        file.write(req.content)


def merge_media(audio_file_path: str, video_file_path: str, file_path: str):
    rst = os.system(
        'ffmpeg-n5.0-latest-win64-lgpl-shared-5.0\\bin\\ffmpeg -i %s -i %s'
        ' -c:v copy -c:a aac -strict experimental %s' % (video_file_path, audio_file_path, file_path))
    if rst != 0:
        raise 'ffmpeg error'
    os.remove(audio_file_path)
    os.remove(video_file_path)


def download_media(bv_id: str, first_cid: int, media_path):
    audio_url, video_url = get_media_url(bv_id, first_cid)
    # download audio
    audio_file_path = 'tmp_audio.m4s'
    download_file(bv_id, audio_url, audio_file_path)
    # download video
    video_file_path = 'tmp_video.m4s'
    download_file(bv_id, video_url, video_file_path)
    # merge media
    file_name = bv_id + '.mp4'
    merge_media(audio_file_path, video_file_path, media_path + file_name)
