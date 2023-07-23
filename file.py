'''
import json
import logging
import os
import re
import time

import api
import request
import sqlite

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
    """确保目录和元数据文件存在，不存在则创建

    :return: None
    """
    global output_path
    global all_path, deleted_path, meta_path, tmp_path

    dao.ensure_directory_and_file()

    # 所有投稿目录\已删除投稿目录\元数据目录\临时数据目录
    output_path = dao.output_path
    all_path = dao.all_path
    meta_path = dao.meta_path
    tmp_path = dao.tmp_path

    deleted_path = os.path.join(output_path, 'deleted')
    os.makedirs(deleted_path, exist_ok=True)

    # 确保元数据(现有、被删除备份、丢失投稿信息和下载目标目录)json文件存在
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
    """
    集合输出为JSON
    """

    def default(self, obj):
        if isinstance(obj, set):
            return str(obj)
        return obj.__dict__


class Limiter:
    def __init__(self, after: int, max_duration: int):
        self.after = after
        self.max_duration = max_duration

    def __str__(self):
        return f'(after: {time.strftime("%Y-%m-%d", time.localtime(self.after))},' \
               f' max_duration: {self.max_duration})'


class Aim:
    def __init__(self, fid: int, limiters: list[Limiter]):
        self.fid = fid
        self.limiters = limiters
        url = api.generate_fav_url(fid)
        resp = request.request_retry_json(url)
        self.title = resp['data']['info']['title']
        self.media_count = resp['data']['info']['media_count']

    def __str__(self):
        limiters = ''
        for i in range(len(self.limiters)):
            limiters += f'\t({i + 1}) {self.limiters[i]}\n'
        return f'收藏夹标题:{self.title} 投稿数:{self.media_count} 收藏夹id:{self.fid}\n{limiters}'


class AimUpper:
    def __init__(self, mid: int, limiters: list[Limiter]):
        self.typ = 'upper'
        self.mid = mid
        self.limiters = limiters
        url = api.generate_user_detail_url(mid)
        resp = request.request_retry_json(url)
        # UP主名字
        logging.debug(f'resp {resp}')
        self.name = resp['data']['name']
        url2 = api.generate_upper_content_url(mid, 1)
        resp2 = request.request_retry_json(url2)
        logging.debug(f'resp2 {resp2}')
        self.media_count = resp2['data']['page']['count']

    def __str__(self):
        limiters = ''
        for i in range(len(self.limiters)):
            limiters += f'\t({i + 1}) {self.limiters[i]}\n'
        return f'UP主ID:{self.mid} 网名:{self.name}\n{limiters}'


class AimMedia:
    def __init__(self, bv_id: str):
        self.typ = 'media'
        self.bv_id = bv_id
        url = api.generate_media_detail_url(bv_id)
        resp = request.request_retry_json(url)
        self.available = resp['code'] == 0
        if self.available:
            # 投稿标题
            self.title = resp['data']['View']['title']
            # 分P数量
            self.media_count = len(resp['data']['View']['pages'])
            self.duration = resp['data']['View']['duration']
            self.pic = resp['data']['View']['pic']
        else:
            # 不可用
            self.title = resp['data']['message']
            self.media_count = 0
            self.duration = 0

    def __str__(self):
        return f'投稿标题:{self.title} 投稿分P数:{self.media_count} 投稿bv id:{self.bv_id}'


def read_aim_json_raw() -> list[dict]:
    with open(aim_json, encoding='utf-8') as f:
        aims: list[dict] = json.load(f)
        return aims


def read_aim_json() -> [list[Aim], list[AimMedia], list[AimUpper]]:
    with open(aim_json, encoding='utf-8') as f:
        aims: list[dict] = json.load(f)
        aim_favorites: list[Aim] = list[Aim]()
        aim_medias: list[AimMedia] = list[AimMedia]()
        aim_upper: list[AimUpper] = list[AimUpper]()
        for aim in aims:
            if 'typ' not in aim.keys():
                # 缺省为目标收藏夹
                limiters = [Limiter(limiter['after'], limiter['max_duration']) for limiter in aim['limiters']]
                aim_favorites.append(Aim(aim['fid'], limiters))
            elif aim['typ'] == 'media':  # 目标投稿
                aim_medias.append(AimMedia(aim['bv_id']))
            elif aim['typ'] == 'upper':  # 目标up主
                limiters = [Limiter(limiter['after'], limiter['max_duration']) for limiter in aim['limiters']]
                aim_upper.append(AimUpper(aim['mid'], limiters))
        return aim_favorites, aim_medias, aim_upper


def write_aim_json(aim_favorites: list[Aim], aim_medias: list[AimMedia], aim_uppers: list[AimUpper]):
    with open(aim_json, 'w', encoding='utf-8') as f:
        json.dump(aim_favorites + aim_medias + aim_uppers, f, cls=MyEncoder, ensure_ascii=False)


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
    # 封面图片
    os.link(source_file_base + '.jpg', destination_file_base + '.jpg')
    # 投稿信息
    os.link(source_file_base + '.json', destination_file_base + '.json')
    # 投稿所有分P
    if page == 1:
        os.link(source_file_base + '.mp4', destination_file_base + '.mp4')
    else:
        for i in range(page):
            os.link(source_file_base + '_' + str(i + 1) + '.mp4', destination_file_base + '_' + str(i + 1) + '.mp4')


def validate_file_name(name: str):
    # 用_替换不能用作文件名的字符 / \ : * ? " < > |
    return re.sub(r"[\/\\\:\*\?\"\<\>\|]", "_", name)


def create_name_file(bv_id: str, page: int, title: str, parts: list[str]):
    name_file_base = os.path.join(deleted_path, bv_id)
    os.mknod(name_file_base + '_' + validate_file_name(title) + '.name')
    if page != 1:
        for i in range(page):
            os.mknod(name_file_base + '_' + str(i + 1) + '_' + validate_file_name(parts[i]))


def write_html(html_content: str):
    # 读模板
    template: str
    with open('template.html', encoding='utf-8') as f:
        template = f.read()
    # 写网页
    with open(os.path.join(meta_path, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(template.replace('<!-- 此处填充投稿内容 -->', html_content))
'''
