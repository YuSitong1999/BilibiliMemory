import datetime
import sqlite3
import pytz

import config


def timestamp_to_time(timestamp: int | str) -> str:
    if timestamp == '':
        return ''
    timestamp = int(timestamp)
    return datetime.datetime.fromtimestamp(timestamp, pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')


class AimLimiter:
    """目标限制类"""

    def __init__(self, id: int, aim_id: int, after: int, max_duration: int):
        self.id: int = id
        self.aim_id: int = aim_id
        self.after: int = after
        self.max_duration: int = max_duration

    def __str__(self):
        return f'{self.id}: {self.aim_id} {timestamp_to_time(self.after)} {self.max_duration}'


def get_all_aim_limiter() -> list[AimLimiter]:
    """获取所有目标限制信息

    :return: 所有目标限制信息
    """
    conn = sqlite3.connect(config.sqlite3_file)
    cursor = conn.cursor()
    aim_limiters = cursor.execute('SELECT * FROM aim_limiter').fetchall()

    cursor.close()
    conn.close()
    result = [AimLimiter(aim_limiter[0], aim_limiter[1], aim_limiter[2], aim_limiter[3]) for aim_limiter in
              aim_limiters]
    return result


def get_aim_limiter_by_aim_id(aim_id: int) -> list[AimLimiter]:
    """获取目标限制信息

    :param aim_id: 目标ID
    :return: 目标限制信息
    """
    conn = sqlite3.connect(config.sqlite3_file)
    cursor = conn.cursor()
    aim_limiters = cursor.execute('SELECT * FROM aim_limiter WHERE aim_id=?', (aim_id,)).fetchall()

    cursor.close()
    conn.close()
    result = [AimLimiter(aim_limiter[0], aim_limiter[1], aim_limiter[2], aim_limiter[3]) for aim_limiter in
              aim_limiters]
    return result


def insert_aim_limiter(aim_id: int, after: int, max_duration: int):
    """插入目标限制信息

    """
    conn = sqlite3.connect(config.sqlite3_file)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO aim_limiter VALUES(NULL, ?, ?, ?)', (aim_id, after, max_duration))
    conn.commit()
    cursor.close()
    conn.close()


def delete_aim_limiter_by_id(id: int):
    """删除目标限制信息

    """
    conn = sqlite3.connect(config.sqlite3_file)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM aim_limiter WHERE id=?', (id,))
    conn.commit()
    cursor.close()
    conn.close()
