import os
import sys
import time
import requests
import json

from media import download_media


class UserSimple:
    def __init__(self, mid: str, name: str):
        self.mid = mid
        self.name = name

    def __str__(self):
        return 'UserSimple: ' + self.mid + ' ' + self.name


class User(UserSimple):
    def __init__(self, mid: str, name: str, sex: str, sign: str):
        super().__init__(mid, name)
        self.sex = sex
        self.sign = sign

    def __str__(self):
        return 'User: ' + self.mid + ' ' + self.name + ' ' + self.sign


class FavFolder:
    def __init__(self, fid: int, mid: int, title: str, media_count: int):
        self.fid = fid
        self.mid = mid
        self.title = title
        self.media_count = media_count

    def __str__(self):
        return 'FavFolder: ' + self.title + ' ' + str(self.media_count)


class Media:
    def __init__(self, id: int, title: str, intro: str, page: int, upper: UserSimple,
                 ctime: int, pubtime: int, fav_time: int, bv_id: str, first_cid: int):
        self.id = id
        self.title = title
        self.intro = intro
        self.page = page
        self.upper = upper

        self.ctime = ctime
        self.pubtime = pubtime
        self.fav_time = fav_time
        self.bv_id = bv_id
        self.first_cid = first_cid


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__


def get_user_info(mid: str) -> User:
    url = 'https://api.bilibili.com/x/space/acc/info?mid=' + mid
    response = requests.get(url)
    response_json = json.loads(response.text)
    if response_json['code'] != 0:
        raise 'get user information error: ' + mid
    user = response_json['data']
    return User(mid, user['name'], user['sex'], user['sign'])


def get_user_created_all_fav_folders(mid: str) -> list[FavFolder]:
    url = 'https://api.bilibili.com/x/v3/fav/folder/created/list-all?up_mid=' + mid
    response = requests.get(url)
    response_json = json.loads(response.text)
    if response_json['code'] != 0:
        raise 'get user favorite folders error: ' + mid
    return [FavFolder(folder['id'], folder['mid'], folder['title'], folder['media_count'])
            for folder in response_json['data']['list']]


def get_user_created_fav_folder_content(folder: FavFolder) -> list[Media]:
    output_folder = 'output\\%s\\%s\\' % (folder.mid, folder.fid)
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    base_url = 'https://api.bilibili.com/x/v3/fav/resource/list?ps=20&keyword=&order=mtime' \
               '&type=0&tid=0&platform=web&jsonp=jsonp&media_id=' + str(folder.fid)
    medias = list[Media]([])
    for i in range(1, (folder.media_count + 20 - 1) // 20 + 1):
        url = base_url + ('&pn=%d' % i)
        response = requests.get(url)
        response_json = json.loads(response.text)
        if response_json['code'] != 0:
            raise 'get favorite folder error: ' + str(folder.fid)
        print(response_json['data'])
        for media in response_json['data']['medias']:
            upper_json = media['upper']
            user_simple = UserSimple(upper_json['mid'], upper_json['name'])
            now_media = Media(media['id'], media['title'], media['intro'], media['page'], user_simple,
                              media['ctime'], media['pubtime'], media['fav_time'], media['bv_id'],
                              media['ugc']['first_cid'])

            download_media(now_media.bv_id, now_media.first_cid, output_folder)

            medias.append(now_media)
            with open(output_folder + 'medias.json', 'w') as f:
                json.dump(medias, f, cls=MyEncoder, ensure_ascii=False)
            print('finished:', folder.title, now_media.title)
            time.sleep(5)
    return medias


def main():
    mid: str = sys.argv[1]

    user = get_user_info(mid)

    folders = get_user_created_all_fav_folders(mid)

    output = 'output\\' + mid + '\\'
    if not os.path.exists(output):
        os.mkdir(output)
    with open(output + 'user.json', 'w') as f:
        json.dump(user, f, cls=MyEncoder, ensure_ascii=False)
    with open(output + 'fav_folders.json', 'w') as f:
        json.dump(folders, f, cls=MyEncoder, ensure_ascii=False)

    for folder in folders:
        get_user_created_fav_folder_content(folder)


if __name__ == '__main__':
    main()
