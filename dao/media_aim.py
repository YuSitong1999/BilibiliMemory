import sqlite3

import config


class MediaAim:
    """投稿所属目标类"""

    def __init__(self, bv_id: str, aim_id: int):
        self.bv_id: str = bv_id
        self.aim_id: int = aim_id


def get_all_media_aim() -> list[MediaAim]:
    """获取所有投稿所属目标信息

    :return: 所有投稿所属目标信息
    """
    conn = sqlite3.connect(config.sqlite3_file)
    cursor = conn.cursor()
    media_aims = cursor.execute('SELECT * FROM media_aim').fetchall()

    cursor.close()
    conn.close()
    result = [MediaAim(media_aim[0], media_aim[1]) for media_aim in media_aims]
    return result


# def insert_media_aim(bv_id: str, aim_id: int):
#     """保存投稿所属目标信息
#
#     """
#     conn = sqlite3.connect(config.sqlite3_file)
#     cursor = conn.cursor()
#     cursor.execute('INSERT INTO media_aim VALUES(?, ?)', (bv_id, aim_id))
#     conn.commit()
#     cursor.close()
#     conn.close()


def save_media_aim(bv_id: str, aim_id: int):
    """保存投稿所属目标信息，如果已存在则不保存

    """
    conn = sqlite3.connect(config.sqlite3_file)
    cursor = conn.cursor()
    cursor.execute('INSERT OR REPLACE INTO media_aim VALUES(?, ?)', (bv_id, aim_id))
    conn.commit()
    cursor.close()
    conn.close()
