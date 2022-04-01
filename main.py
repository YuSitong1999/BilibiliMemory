import os
import sys
import requests
import json


class User:
    def __init__(self, mid: str, name: str, sex: str, sign: str):
        self.mid = mid
        self.name = name
        self.sex = sex
        self.sign = sign

    def __str__(self):
        return 'User: ' + self.name + ' ' + self.sign


class FavFolder:
    def __init__(self, fid: int, mid: int, title: str, media_count: int):
        self.fid = fid
        self.mid = mid
        self.title = title
        self.media_count = media_count

    def __str__(self):
        return 'FavFolder: ' + self.title + ' ' + str(self.media_count)


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


if __name__ == '__main__':
    main()
