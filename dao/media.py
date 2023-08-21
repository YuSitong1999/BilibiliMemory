import math
import sqlite3
import time

import config


class Media:
    """投稿类"""

    def __init__(self, bv_id: str, up_id: int, title: str, introduction: str, duration: int, create_time: int,
                 favorite_time: int, download_time: int, is_local: bool, is_delete: bool):
        self.bv_id: str = bv_id
        self.up_id: int = up_id
        self.title: str = title
        self.introduction: str = introduction
        self.duration: int = duration
        self.create_time: int = create_time
        self.favorite_time: int = favorite_time
        self.update_time: int = download_time
        self.is_local: bool = is_local
        self.is_delete: bool = is_delete


def get_all_media() -> list[Media]:
    """获取所有投稿信息

    :return: 所有投稿信息
    """
    conn = sqlite3.connect(config.sqlite3_file)
    cursor = conn.cursor()
    medias = cursor.execute('SELECT * FROM media').fetchall()

    cursor.close()
    conn.close()
    result = [Media(media[0], media[1], media[2], media[3], media[4], media[5], media[6], media[7], media[8], media[9])
              for media in medias]
    return result


def get_media_by_bv_id(bv_id: str) -> Media | None:
    """根据BV号获取投稿信息

    :param bv_id: BV号
    :return: 投稿信息
    """
    conn = sqlite3.connect(config.sqlite3_file)
    cursor = conn.cursor()
    media = cursor.execute('SELECT * FROM media WHERE bv_id=?', (bv_id,)).fetchone()

    cursor.close()
    conn.close()
    if media is None:
        return None
    return Media(media[0], media[1], media[2], media[3], media[4], media[5], media[6], media[7], media[8], media[9])


def insert_or_replace_media(bv_id: str, up_id: int, title: str, introduction: str, duration: int, create_time: int,
                            favorite_time: int, download_time: int, is_local: bool, is_delete: bool):
    """插入投稿信息

     """
    conn = sqlite3.connect(config.sqlite3_file)
    cursor = conn.cursor()
    cursor.execute('INSERT OR REPLACE INTO media VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                   (bv_id, up_id, title, introduction, duration, create_time, favorite_time, download_time, is_local,
                    is_delete))
    conn.commit()
    cursor.close()
    conn.close()


def update_media(bv_id: str, up_id: int, title: str, introduction: str, duration: int, create_time: int,
                 favorite_time: int, update_time: int, is_local: bool, is_delete: bool):
    """更新投稿信息

    """
    conn = sqlite3.connect(config.sqlite3_file)
    cursor = conn.cursor()
    cursor.execute('UPDATE media SET up_id=?, title=?, introduction=?, duration=?, create_time=?, favorite_time=?, '
                   'update_time=?, is_local=?, is_delete=? WHERE bv_id=?',
                   (up_id, title, introduction, duration, create_time, favorite_time, update_time, is_local,
                    is_delete, bv_id))
    conn.commit()
    cursor.close()
    conn.close()


def update_media_status(bv_id: str, is_local: bool, is_delete: bool):
    """更新投稿状态

    """
    conn = sqlite3.connect(config.sqlite3_file)
    cursor = conn.cursor()
    update_time = math.floor(time.time())
    cursor.execute('UPDATE media SET update_time=?, is_local=?, is_delete=? WHERE bv_id=?',
                   (update_time, is_local, is_delete, bv_id))
    conn.commit()
    cursor.close()
    conn.close()
