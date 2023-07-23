import math
import sqlite3
import time

import config


class Aim:
    """目标类"""

    def __init__(self, id: int, type: int, target_id: int, name: str, update_time: int):
        self.id: int = id
        self.type: int = type
        self.target_id: int = target_id
        self.name: str = name
        self.update_time: int = update_time

    def __str__(self):
        return f'{self.id}: {self.target_id} {self.name} {self.update_time}'


def get_all_aim() -> list[Aim]:
    """获取所有目标信息

    :return: 所有目标信息
    """
    conn = sqlite3.connect(config.sqlite3_file)
    cursor = conn.cursor()
    aims = cursor.execute('SELECT * FROM aim').fetchall()

    cursor.close()
    conn.close()
    result = [Aim(aim[0], aim[1], aim[2], aim[3], aim[4]) for aim in aims]
    return result


def get_aim_by_type_and_target_id(type: int, target_id: int) -> Aim | None:
    """根据类型和目标ID获取目标信息

    :param type: 类型
    :param target_id: 目标ID
    :return: 目标信息
    """
    conn = sqlite3.connect(config.sqlite3_file)
    cursor = conn.cursor()
    aim = cursor.execute('SELECT * FROM aim WHERE `type`=? AND target_id=?', (type, target_id)).fetchone()

    cursor.close()
    conn.close()
    if aim is None:
        return None
    return Aim(aim[0], aim[1], aim[2], aim[3], aim[4])


def insert_or_replace_aim(type: int, target_id: int, name: str):
    """插入目标信息

    """
    conn = sqlite3.connect(config.sqlite3_file)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO aim VALUES(NULL, ?, ?, ?, ?)', (type, target_id, name, math.floor(time.time())))
    conn.commit()
    cursor.close()
    conn.close()


def update_aim_by_id(id: int, name: str, update_time: int):
    """更新目标信息

    """
    conn = sqlite3.connect(config.sqlite3_file)
    cursor = conn.cursor()
    cursor.execute('UPDATE aim SET name=?, update_time=? WHERE id=?', (name, update_time, id))
    conn.commit()
    cursor.close()
    conn.close()


def delete_aim_by_id(id: int):
    """删除目标信息

    """
    conn = sqlite3.connect(config.sqlite3_file)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM aim WHERE id=?', (id,))
    conn.commit()
    cursor.close()
    conn.close()
