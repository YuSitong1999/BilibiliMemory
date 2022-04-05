import json
import logging
import os
import time

import config
import request

output_path: str = 'output'

all_path: str = ''
deleted_path: str = ''
meta_path: str = ''
tmp_path: str = ''

local_json: str = ''
lost_json: str = ''
aim_json: str = ''


def ensure_json_list_exist(file_path: str):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            json.dump([], f, ensure_ascii=False)


def ensure_directory_and_file():
    global output_path
    global all_path, deleted_path, meta_path, tmp_path

    # ensure directory
    os.makedirs(output_path, exist_ok=True)
    all_path = os.path.join(output_path, 'all')
    deleted_path = os.path.join(output_path, 'deleted')
    meta_path = os.path.join(output_path, 'meta')
    tmp_path = os.path.join(output_path, 'tmp')

    os.makedirs(all_path, exist_ok=True)
    os.makedirs(deleted_path, exist_ok=True)
    os.makedirs(meta_path, exist_ok=True)
    os.makedirs(tmp_path, exist_ok=True)

    # ensure json file
    global local_json, lost_json, aim_json
    local_json = os.path.join(meta_path, 'local.json')
    lost_json = os.path.join(meta_path, 'lost.json')
    aim_json = os.path.join(meta_path, 'aim.json')
    ensure_json_list_exist(local_json)
    ensure_json_list_exist(lost_json)
    ensure_json_list_exist(aim_json)


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return str(obj)
        return obj.__dict__


class Aim:
    def __init__(self, fid: int, after: int, limit: int):
        self.fid = fid
        self.after = after
        self.limit = limit
        url = 'https://api.bilibili.com/x/v3/fav/resource/list?media_id=%d&pn=1&ps=20&keyword=&order=mtime&type=0&tid' \
              '=0&platform=web&jsonp=jsonp' % fid
        self.title = request.request(url)['data']['info']['title']

    def __str__(self):
        return 'fid:%d after:%s limit:%d title:%s' % \
               (self.fid, time.strftime('%Y-%m-%d', time.localtime(self.after)), self.limit, self.title)


def read_aim_json() -> list[Aim]:
    with open(aim_json, encoding='utf-8') as f:
        aims: list[dict] = json.load(f)
        return [Aim(aim['fid'], aim['after'], aim['limit']) for aim in aims]


def write_aim_json(aims: list[Aim]):
    with open(aim_json, 'w', encoding='utf-8') as f:
        json.dump(aims, f, cls=MyEncoder, ensure_ascii=False)


def read_local_file() -> tuple[list[dict], list[dict], list[dict], list[dict]]:
    logging.info('read_local_file')
    # read media file
    with open(config.media_file, encoding='utf-8') as f:
        media: dict = json.load(f)
        media_exist: list[dict] = media['exist']
        media_deleted: list[dict] = media['deleted']

    logging.info('read_local_file media_exist')
    logging.info(json.dumps(media_exist))
    logging.info('read_local_file media_deleted')
    logging.info(json.dumps(media_deleted))
    # read folder file
    with open(config.folder_file, encoding='utf-8') as f:
        folder: list[dict] = json.load(f)
    logging.info('read_local_file folder')
    logging.info(json.dumps(folder))
    # read lost file
    with open(config.lost_file, encoding='utf-8') as f:
        lost: list[dict] = json.load(f)
    logging.info('read_local_file lost')
    logging.info(json.dumps(lost))
    return media_exist, media_deleted, folder, lost


def write_json_file(path: str, obj: object):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, cls=MyEncoder, ensure_ascii=False)


def write_local_file(local_exist: list[dict], local_deleted: list[dict]):
    write_json_file(config.media_file, {'exist': local_exist, 'deleted': local_deleted})


def write_folder_file(folder: list[object]):
    write_json_file(config.folder_file, folder)


def write_lost_file(lost: list[dict]):
    write_json_file(config.lost_file, lost)
