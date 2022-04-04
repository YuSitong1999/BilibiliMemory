import json
import logging
import config


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__


def read_local_file() -> tuple[list[dict], list[dict], list[dict], list[dict]]:
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
