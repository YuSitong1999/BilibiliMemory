import logging
import math
import os
import re
import shutil
import sys
import time
import requests
import json
import file
from media import download_media, download_file
from file import read_local_file, MyEncoder
import config


class UserSimple:
    def __init__(self, mid: int, name: str):
        self.mid = mid
        self.name = name


class User:
    def __init__(self, mid: int):
        self.mid = mid
        self.name, self.sex, self.sign = api_get_user(mid)
        logging.info('set user name: ' + self.name)
        self.fav_folders = api_get_user_all_folders(mid)


class FavFolder:
    def __init__(self, fid: int, mid: int, title: str, media_count: int):
        self.fid = fid
        self.mid = mid
        self.title = title
        self.media_count = media_count
        logging.info('set fav_folder title: ' + self.title)
        self.medias = api_get_folder_all_medias(fid, media_count)


class Media:
    def __init__(self, id: int, title: str, intro: str, page: int, duration: int, upper: UserSimple,
                 ctime: int, pubtime: int, fav_time: int, bv_id: str, first_cid: int, cover: str):
        self.page = 0
        # if fav_time < config.after_time_stamp: TODO skip media a long time ago
        #     logging.info('skip media title: ' + self.title)
        #     return
        self.id = id
        self.title = title
        self.intro = intro
        self.page = page
        self.duration = duration  # TODO auto or ask user skip too long media
        self.upper = upper

        self.ctime = ctime
        self.pubtime = pubtime
        self.fav_time = fav_time
        self.bv_id = bv_id
        self.first_cid = first_cid
        self.cover = cover

        self.pages = []
        logging.info('set media title: ' + self.title)
        self.pages = api_get_media_all_pages(bv_id)


class Page:
    def __init__(self, cid: int, part: str, duration: int):
        self.cid = cid
        self.part = part
        self.duration = duration


def api_get_user(mid: int) -> tuple[str, str, str]:
    url = 'https://api.bilibili.com/x/space/acc/info?jsonp=jsonp&mid=%s' % mid
    resp = json.loads(requests.get(url, headers={'Connection': 'close'}).text)
    if resp['code'] != 0:
        raise Exception('get user information error: ' + str(mid))
    user = resp['data']
    return user['name'], user['sex'], user['sign']


def api_get_user_all_folders(mid: int) -> list[FavFolder]:
    url = 'https://api.bilibili.com/x/v3/fav/folder/created/list-all?jsonp=jsonp&up_mid=%s' % mid
    resp = json.loads(requests.get(url, headers={'Connection': 'close'}).text)
    if resp['code'] != 0:
        raise Exception('get user favorite folders error: ' + str(mid))
    return [FavFolder(folder['id'], folder['mid'], folder['title'], folder['media_count'])
            for folder in resp['data']['list']]


def api_get_folder_all_medias(fid: int, media_count: int) -> list[Media]:
    def generate_url(page_number: int):
        return 'https://api.bilibili.com/x/v3/fav/resource/list?ps=20&keyword=&order=mtime' \
               '&type=0&tid=0&platform=web&jsonp=jsonp&media_id=%d&pn=%d' % (fid, page_number)

    medias = list[Media]([])
    page_count = math.ceil(media_count / 20)
    for page_id in range(page_count):
        url = generate_url(page_id)
        resp = json.loads(requests.get(url, headers={'Connection': 'close'}).text)
        if resp['code'] != 0:
            raise Exception('get favorite folder error: ' + str(fid))

        for media in resp['data']['medias']:
            upper = media['upper']
            user_simple = UserSimple(upper['mid'], upper['name'])
            now_media = Media(media['id'], media['title'], media['intro'], media['page'], media['duration'],
                              user_simple, media['ctime'], media['pubtime'], media['fav_time'], media['bv_id'],
                              media['ugc']['first_cid'], media['cover'])
            medias.append(now_media)
            time.sleep(1)

        time.sleep(5)

    return medias


def api_get_media_all_pages(bv_id: str) -> list[Page]:
    pages: list[Page] = []
    url = 'https://api.bilibili.com/x/player/pagelist?jsonp=jsonp&bvid=%s' % bv_id
    resp = json.loads(requests.get(url, headers={'Connection': 'close'}).text)
    if resp['code'] == -404:
        return []
    elif resp['code'] != 0:
        raise Exception('get media pages error: ' + bv_id)
    for p in resp['data']:
        page = Page(p['cid'], p['part'], p['duration'])
        pages.append(page)
    return pages


# get all information about aim users' favorite
def get_users() -> list[User]:
    logging.info('get_users:')
    users: list[User] = list[User]()
    for mid in config.id_list:
        users.append(User(mid))
    logging.info('update_get users: ')
    logging.info(json.dumps(users, cls=MyEncoder, ensure_ascii=False))
    return users


def generate_set_from_list(medias: list[dict]) -> set[str]:
    st: set[str] = set[str]()
    for media in medias:
        st.add(media['bv_id'])
    return st


def generate_list_use_set_from_dict(s: set[str], d: dict[str, object]) -> list[object]:
    return [d[key] for key in s]


def validate_file_name(name: str):
    # replace / \ : * ? " < > | with _
    return re.sub(r"[\/\\\:\*\?\"\<\>\|]", "_", name)


def create_link_from_path_to_media(bv_id: str, page: int, title: str, path: str):
    source_file_base = os.path.join(config.output_all_path, bv_id)
    destination_file_base = os.path.join(path, bv_id + '_' + validate_file_name(title))
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


def delete_media_from_all(bv_id: str, page: int):
    source_file_base = os.path.join(config.output_all_path, bv_id)
    # delete cover jpg
    os.remove(source_file_base + '.jpg')
    # delete information json
    os.remove(source_file_base + '.json')
    # delete media pages
    if page == 1:
        os.remove(source_file_base + '.mp4')
    else:
        for i in range(page):
            os.remove(source_file_base + '_' + str(i + 1) + '.mp4')


def update_all_and_delete_path() -> list[User]:
    logging.info('begin update all and delete path:')
    # read media folder lost
    local_exist, local_deleted, local_folder, local_lost = read_local_file()
    new_local_exist = local_exist.copy()
    new_local_deleted = local_deleted.copy()

    # generate local
    local_exist_set: set[str] = generate_set_from_list(local_exist)
    local_deleted_set: set[str] = generate_set_from_list(local_deleted)

    local_lost_set: set[str] = generate_set_from_list(local_lost)

    users: list[User] = get_users()

    # put online media into all_media
    all_media: dict[str, Media] = {}
    # generate online exist and deleted set
    online_exist_set: set[str] = set[str]()
    online_deleted_set: set[str] = set[str]()
    for i in range(len(users)):
        for j in range(len(users[i].fav_folders)):
            new_medias: list[Media] = []
            for media in users[i].fav_folders[j].medias:
                if media.page == 0:
                    # manually skip media
                    continue
                all_media[media.bv_id] = media
                if len(media.pages) == 0:
                    # deleted
                    online_deleted_set.add(media.bv_id)
                    continue
                # exist now
                online_exist_set.add(media.bv_id)
                new_medias.append(media)
            # filter skip media
            users[i].fav_folders[j].medias = new_medias
    logging.info('users')
    logging.info(json.dumps(users, cls=MyEncoder, ensure_ascii=False))

    # put local media into all_media
    for media in local_exist + local_deleted:
        bv_id = media['bv_id']
        all_media[bv_id] = Media(media['id'], media['title'], media['intro'], media['page'], media['duration'],
                                 UserSimple(media['upper']['mid'], media['upper']['name']), media['ctime'],
                                 media['pubtime'], media['fav_time'], media['bv_id'], media['first_cid'],
                                 media['cover'])
    logging.debug('all_media: ' + object_to_json_str(all_media))

    '''
    update lost media information
    '''
    logging.info('start update lost media')
    new_lost_set = online_deleted_set.difference(local_exist_set). \
        difference(local_deleted_set).difference(local_lost_set)
    new_lost = generate_list_use_set_from_dict(new_lost_set, all_media)
    local_lost += new_lost
    file.write_lost_file(local_lost)
    logging.info('finished update lost media')

    '''
    download new favorite media
    '''
    logging.info('start download new favorite media')
    new_favorite_set = online_exist_set.difference(local_exist_set).difference(local_deleted_set)
    is_first = True
    for bv_id in new_favorite_set:
        if is_first:
            is_first = False
        else:
            # sleep to avoid block
            time.sleep(10)

        now_media = all_media[bv_id]
        # download cover picture
        download_file(bv_id, now_media.cover, os.path.join(config.output_all_path, bv_id + '.jpg'))
        # save media information to json file
        file.write_json_file(os.path.join(config.output_all_path, bv_id + '.json'), now_media)
        # download medias of all pages
        cid_list: list[int] = [page.cid for page in now_media.pages]
        logging.info('cid_list')
        logging.info(cid_list)
        for i in range(len(cid_list)):
            cid = cid_list[i]
            if i != 0:
                time.sleep(3)

            page_id = str(i + 1)
            if len(cid_list) == 1:
                page_id = ''
            download_media(bv_id, cid, config.output_all_path, page_id)
        new_local_exist.append(now_media.__dict__)
        # update media.json immediately
        file.write_local_file(new_local_exist, new_local_deleted)
    logging.info('finished download new favorite media')

    '''
    create hard link for nearly deleted files
    '''
    nearly_deleted_set = local_exist_set.intersection(online_deleted_set)
    for bv_id in nearly_deleted_set:
        now_media = all_media[bv_id]
        create_link_from_path_to_media(bv_id, now_media.page, now_media.title, config.output_deleted_path)
        new_local_deleted.append(now_media.__dict__)
        new_local_exist = [e for e in new_local_exist if e['bv_id'] != bv_id]
        file.write_local_file(new_local_exist, new_local_deleted)

    '''
    nearly disappear favorite media
    '''
    nearly_cancel_favorite_set = local_exist_set.difference(online_exist_set).difference(online_deleted_set)
    # cancel favorite: delete local file TODO choose by user
    for bv_id in nearly_cancel_favorite_set:
        now_media = all_media[bv_id]
        new_local_exist = [e for e in new_local_exist if e['bv_id'] != bv_id]
        file.write_local_file(new_local_exist, new_local_deleted)
        delete_media_from_all(bv_id, now_media.page)
        # TODO unknown: maybe cancel before deleted

    # TODO available again
    '''
    available again
    '''

    return users


def update_local_user_folder(users: list[User]):
    # delete old and create new
    for user in users:
        user_path = os.path.join(config.output_path, str(user.mid))
        if os.path.exists(user_path):
            shutil.rmtree(user_path)
        os.mkdir(user_path)
        for folder in user.fav_folders:
            user_folder_path = os.path.join(config.output_path, str(user.mid), str(folder.fid))
            os.mkdir(user_folder_path)
            for media in folder.medias:
                create_link_from_path_to_media(media.bv_id, media.page, media.title, user_folder_path)
    file.write_folder_file(users)


def update_main():
    # configure
    config.ensure_config()

    users = update_all_and_delete_path()

    update_local_user_folder(users)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(name)s %(levelname)s %(message)s",
                        datefmt='%Y-%m-%d  %H:%M:%S %a'
                        )

    opt = sys.argv[1]
    if opt == 'update':
        update_main()
    elif opt == 'clean':
        pass  # clean useless files after exception
    elif opt == 'check':
        pass  # check whether the mate data match the actual files or not
