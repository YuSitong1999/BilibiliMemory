import json
import os
import re
import time

import request

output_path: str = 'output'

all_path: str = ''
deleted_path: str = ''
meta_path: str = ''
tmp_path: str = ''

local_json: str = ''
deleted_json: str = ''
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
    global local_json, deleted_json, lost_json, aim_json
    local_json = os.path.join(meta_path, 'local.json')
    deleted_json = os.path.join(meta_path, 'deleted.json')
    lost_json = os.path.join(meta_path, 'lost.json')
    aim_json = os.path.join(meta_path, 'aim.json')
    ensure_json_list_exist(local_json)
    ensure_json_list_exist(deleted_json)
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
        resp = request.request_retry_json(url)
        self.title = resp['data']['info']['title']
        self.media_count = resp['data']['info']['media_count']

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


def read_local_json() -> set[str]:
    with open(local_json, encoding='utf-8') as f:
        local_bv_id_list: list[str] = json.load(f)
        return set[str](local_bv_id_list)


def read_deleted_json() -> set[str]:
    with open(deleted_json, encoding='utf-8') as f:
        deleted_bv_id_list: list[str] = json.load(f)
        return set[str](deleted_bv_id_list)


def read_lost_json() -> list:
    with open(lost_json, encoding='utf-8') as f:
        lost_list: list = json.load(f)
        return lost_list


def read_media_json(bv_id: str) -> dict:
    with open(os.path.join(all_path, bv_id + '.json'), encoding='utf-8') as f:
        media: dict = json.load(f)
        return media


def write_json_file(path: str, obj: object):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, cls=MyEncoder, ensure_ascii=False)


def write_local_json(local: list[str]):
    write_json_file(local_json, local)


def write_deleted_json(deleted: list[str]):
    write_json_file(deleted_json, deleted)


def write_lost_json(lost: list[dict]):
    write_json_file(lost_json, lost)


def create_link_from_all_to_deleted(bv_id: str, page: int):
    source_file_base = os.path.join(all_path, bv_id)
    destination_file_base = os.path.join(deleted_path, bv_id)
    # cover jpg
    os.link(source_file_base + '.jpg', destination_file_base + '.jpg')
    # information
    os.link(source_file_base + '.json', destination_file_base + '.json')
    # media pages
    if page == 1:
        os.link(source_file_base + '.mp4', destination_file_base + '.mp4')
    else:
        for i in range(page):
            os.link(source_file_base + '_' + str(i + 1) + '.mp4', destination_file_base + '_' + str(i + 1) + '.mp4')


def validate_file_name(name: str):
    # replace / \ : * ? " < > | with _
    return re.sub(r"[\/\\\:\*\?\"\<\>\|]", "_", name)


def create_name_file(bv_id: str, page: int, title: str, parts: list[str]):
    name_file_base = os.path.join(deleted_path, bv_id)
    os.mknod(name_file_base + '_' + validate_file_name(title) + '.name')
    if page != 1:
        for i in range(page):
            os.mknod(name_file_base + '_' + str(i + 1) + '_' + validate_file_name(parts[i]))
