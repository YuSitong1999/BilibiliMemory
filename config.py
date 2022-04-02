import configparser
import json
import logging
import math
import os
import time
import os.path

config_path = 'config.ini'
config = configparser.ConfigParser()

output_path: str
output_all_path: str
output_deleted_path: str

meta_path: str
tmp_path: str
media_file: str
folder_file: str
lost_file: str

id_list: list[int]
after_time_stamp: int


def create_initial_config():
    config.read(config_path)
    config.set('path', 'output', 'output')
    config.set('path', 'meta', 'output')
    config.set('path', 'tmp', 'output')
    config.set('task', 'id', '')

    local_date = time.strftime("%Y-%m-%d", time.localtime())
    logging.info('local_date: ', local_date)
    config.set('task', 'after', local_date)
    print('cannot find config.ini, new config.ini is created!')


def ensure_json_list_exist(file_path: str, content: object):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            json.dump(content, f, ensure_ascii=False)


def ensure_path_exist(path: str):
    if not os.path.exists(path):
        os.makedirs(path)


def ensure_id_list():
    global id_list
    id_str_list = config.get('task', 'id').split(',')
    while True:
        try:
            id_str_list.remove('')
        except ValueError:
            break

    id_list = []
    for id in id_str_list:
        if id.isdigit():
            id_list.append(int(id))

    if len(id_list) == 0:
        raise Exception('aim user id is empty')
    logging.info('task id: ')
    logging.info(id_str_list)


def ensure_config():
    global config_path, config
    global output_path, output_all_path, output_deleted_path
    global meta_path, tmp_path
    global media_file, folder_file, lost_file
    global after_time_stamp
    if not os.path.exists(config_path):
        create_initial_config()
    else:
        config.read(config_path)

    # ensure path
    output_path = config.get('path', 'output')
    ensure_path_exist(output_path)
    output_all_path = os.path.join(output_path, 'all')
    ensure_path_exist(output_all_path)
    output_deleted_path = os.path.join(output_path, 'deleted')
    ensure_path_exist(output_deleted_path)

    meta_path = config.get('path', 'meta')
    ensure_path_exist(meta_path)
    tmp_path = config.get('path', 'tmp')
    ensure_path_exist(tmp_path)

    # ensure meta json file
    media_file = os.path.join(meta_path, 'media.json')
    ensure_json_list_exist(media_file, {'exist': [], 'deleted': []})
    folder_file = os.path.join(meta_path, 'folder.json')
    ensure_json_list_exist(folder_file, [])
    lost_file = os.path.join(meta_path, 'lost.json')
    ensure_json_list_exist(lost_file, [])

    # ensure id
    ensure_id_list()

    after_time_stamp = math.floor(time.mktime(time.strptime(config.get('task', 'after'), "%Y-%m-%d")))
    logging.info('after_time_stamp: ')
    logging.info(after_time_stamp)
    config.set('task', 'stamp', str(after_time_stamp))
