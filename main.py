import getopt
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
        logging.info('NOW USER NAME: ' + self.name)
        self.fav_folders = api_get_user_all_folders(mid)
        # filter skipped favorite folder
        now_folders: list[FavFolder] = []
        for i in range(len(self.fav_folders)):
            if len(self.fav_folders[i].medias) != 0:
                now_folders.append(self.fav_folders[i])
        self.fav_folders = now_folders


class FavFolder:
    def __init__(self, fid: int, mid: int, title: str, media_count: int):
        self.fid = fid
        self.mid = mid
        self.title = title
        self.media_count = 0
        self.medias = []
        logging.info('NOW FAVORITE FOLDER TITLE: ' + self.title)
        is_skip = input('skip favorite folder %s y(es) or not(default)?' % self.title).strip().lower()
        if is_skip != '' and is_skip[0] == 'y':
            return
        self.media_count = media_count
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


def object_to_json_str(obj: object) -> str:
    return json.dumps(obj, cls=MyEncoder, ensure_ascii=False)


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
            logging.info('sleep for 1s')
            time.sleep(1)
        logging.info('sleep for 5s')
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
    logging.info('GET ALL USERS:')
    users: list[User] = list[User]()
    for mid in config.id_list:
        users.append(User(mid))
    logging.info('GET ALL USERS FINISHED.')
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
    logging.info('remove media: ' + source_file_base)
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
    logging.info('UPDATE ALL AND DELETE DIRECTORY:')
    # read media folder lost
    local_exist, local_deleted, local_folder, local_lost = read_local_file()
    logging.debug('local_exist: ' + object_to_json_str(local_exist))
    logging.debug('local_deleted: ' + object_to_json_str(local_deleted))
    logging.debug('local_lost: ' + object_to_json_str(local_lost))
    new_local_exist = local_exist.copy()
    new_local_deleted = local_deleted.copy()

    # generate local
    logging.info('generate local set: exist set and deleted set')
    local_exist_set: set[str] = generate_set_from_list(local_exist)
    local_deleted_set: set[str] = generate_set_from_list(local_deleted)

    local_lost_set: set[str] = generate_set_from_list(local_lost)

    logging.debug('local_exist_set: ' + object_to_json_str(local_exist_set))
    logging.debug('local_deleted_set: ' + object_to_json_str(local_deleted_set))
    logging.debug('local_lost_set: ' + object_to_json_str(local_lost_set))

    # get users
    users: list[User] = get_users()

    # put online media into all_media
    all_media: dict[str, Media] = {}
    # generate online exist and deleted set
    online_exist_set: set[str] = set[str]()
    online_deleted_set: set[str] = set[str]()
    logging.info('get all media information, and generate oneline exist set and deleted set:')
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
    logging.info('USER (AFTER FILTER SKIPPED FOLDERS): ')
    logging.debug(object_to_json_str(users))
    logging.debug('online_exist_set: ' + object_to_json_str(online_exist_set))
    logging.debug('online_deleted_set: ' + object_to_json_str(online_deleted_set))

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
    logging.info('update lost media:')
    new_lost_set = online_deleted_set.difference(local_exist_set). \
        difference(local_deleted_set).difference(local_lost_set)
    new_lost = generate_list_use_set_from_dict(new_lost_set, all_media)
    local_lost += new_lost
    file.write_lost_file(local_lost)
    logging.info('update lost media finished.')

    '''
    download new favorite media
    '''
    logging.info('download new favorite media:...')
    new_favorite_set = online_exist_set.difference(local_exist_set).difference(local_deleted_set)
    is_first = True
    for bv_id in new_favorite_set:
        if is_first:
            is_first = False
        else:
            logging.info('sleep for 10s')
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
                logging.info('sleep for 3s')
                time.sleep(3)

            page_id = str(i + 1)
            if len(cid_list) == 1:
                page_id = ''
            download_media(bv_id, cid, config.output_all_path, page_id)
        new_local_exist.append(now_media.__dict__)
        # update media.json immediately
        file.write_local_file(new_local_exist, new_local_deleted)
    logging.info('download new favorite media finished.')

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
        logging.info('delete cancel favorite media: ' + now_media.title)
        delete_media_from_all(bv_id, now_media.page)
        # TODO unknown: maybe cancel before deleted

    # TODO available again
    '''
    available again
    '''

    logging.info('UPDATE ALL AND DELETE DIRECTORY FINISHED.')
    return users


def update_local_user_folder(users: list[User]):
    # delete old and create new
    for user in users:
        user_path = os.path.join(config.output_path, str(user.mid))
        config.ensure_path_exist(user_path)
        for folder in user.fav_folders:
            user_folder_path = os.path.join(config.output_path, str(user.mid), str(folder.fid))
            if os.path.exists(user_folder_path):
                shutil.rmtree(user_folder_path)
            os.mkdir(user_folder_path)
            for media in folder.medias:
                create_link_from_path_to_media(media.bv_id, media.page, media.title, user_folder_path)
    file.write_folder_file(users)


def meta_main(argv: list[str]):
    OPERATION_STATUS = 'status'
    OPERATION_ADD = 'add'
    OPERATION_RM = 'rm'

    try:
        opts, args = getopt.getopt(argv, "o:f:t:l:", [])
    except getopt.GetoptError:
        print('''
    python main.py meta
        -o [add | rm | status]
        [-f <folderID1>[,<folderID2>,...,<folderIDn>]]
        [-t <afterDate>]
        [-l <lengthLimit>]
    ''')
        sys.exit(2)
    operation: str = OPERATION_STATUS
    folders_id: list[int] = []
    after_date: int = 0
    length_limit: int = 0
    for opt, arg in opts:
        if opt == '-o':
            if arg in (OPERATION_ADD, OPERATION_RM):
                operation = arg
        elif opt == '-f':
            folders_id = [int(s) for s in arg.split(',') if s.isnumeric()]
        elif opt == '-t':
            after_date = math.floor(time.mktime(time.strptime(arg, '%Y-%m-%d')))
        elif opt == '-l':
            length_limit = int(arg) if arg.isnumeric() else 0
    aims = file.read_aim_json()
    if operation == OPERATION_STATUS:
        aims_len = len(aims)
        if aims_len == 0:
            print('aim folder id list is empty!')
        for i in range(aims_len):
            print('%d: %s' % (i + 1, aims[i]))
        return
    if len(folders_id) == 0:
        print('folder id list is empty!')
        return
    if operation == OPERATION_ADD:
        for fid in folders_id:
            aims.append(file.Aim(fid, after_date, length_limit))
    else:
        aims = [aim for aim in aims if aim.fid not in folders_id]

    file.write_aim_json(aims)


def append_media_file_name_to_list(name_list: list[str], name: str, page: int):
    name_list.append(name + '.json')
    name_list.append(name + '.jpg')
    if page == 1:
        name_list.append(name + '.mp4')
    else:
        for i in range(page):
            name_list.append('%s_%d.mp4' % (name, i + 1))


def delete_file_name_start_with_bv_and_not_in_list(name_list: list[str], root_path: str):
    for name in os.listdir(root_path):
        path = os.path.join(root_path, name)
        if os.path.isfile(path) and name.find('BV') == 0 and name not in name_list:
            logging.info('remove: ' + path)
            os.remove(path)


def clean_main():
    # read local file
    local_exist, local_deleted, local_folder, local_lost = read_local_file()

    '''
    clean all and delete directory
    '''
    # generate file name in 'all' directory
    all_file_name: list[str] = []
    for media in local_exist + local_deleted:
        bv_id: str = media['bv_id']
        append_media_file_name_to_list(all_file_name, bv_id, media['page'])
    logging.debug('file name should in all directory: ' + object_to_json_str(all_file_name))

    # generate file name in 'deleted' directory
    deleted_file_name: list[str] = []
    for media in local_deleted:
        bv_id: str = media['bv_id']
        file_name_base = bv_id + '_' + validate_file_name(media['title'])
        append_media_file_name_to_list(deleted_file_name, file_name_base, media['page'])
    logging.debug('file name should in deleted directory: ' + object_to_json_str(deleted_file_name))

    # delete media files in all and deleted directory but not in media.json
    logging.info('deleted useless file in all and deleted directory:...')
    delete_file_name_start_with_bv_and_not_in_list(all_file_name, config.output_all_path)
    delete_file_name_start_with_bv_and_not_in_list(deleted_file_name, config.output_deleted_path)
    logging.info('deleted useless file in all and deleted directory finished.')

    # delete files which name start with 'tmp' in tmp directory
    logging.info('deleted useless file in tmp directory:...')
    for name in os.listdir(config.tmp_path):
        path = os.path.join(config.tmp_path, name)
        if os.path.isfile(path) and name.find('tmp') == 0:
            logging.info('remove: ' + path)
            os.remove(path)
    logging.info('deleted useless file in tmp directory finished.')


def set_log():
    log_file_path = os.path.join(file.tmp_path, time.strftime('%Y-%m-%d_%H_%M_%S.log'))
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename=log_file_path,
                        filemode='w'
                        )
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console_handler.setFormatter(formatter)
    logging.getLogger('').addHandler(console_handler)


if __name__ == '__main__':
    file.ensure_directory_and_file()
    set_log()

    opt = sys.argv[1]
    if opt == 'meta':
        logging.info('YOU CHOSE META')
        logging.info('------------------')
        meta_main(sys.argv[2:])
    elif opt == 'update':
        logging.info('YOU CHOSE CLEAN')
        logging.info('------------------')
        clean_main()
