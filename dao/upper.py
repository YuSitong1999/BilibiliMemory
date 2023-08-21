import sqlite3

import config


class Upper:
    """UP主类"""

    def __init__(self, id: int, name: str, introduction: str, update_time: int):
        self.id: int = id
        self.name: str = name
        self.introduction: str = introduction
        self.update_time: int = update_time


def get_all_upper() -> list[Upper]:
    """获取所有UP主信息

    :return: 所有UP主信息
    """
    conn = sqlite3.connect(config.sqlite3_file)
    cursor = conn.cursor()
    uppers = cursor.execute('SELECT * FROM upper').fetchall()

    cursor.close()
    conn.close()
    result = [Upper(upper[0], upper[1], upper[2], upper[3]) for upper in uppers]
    return result


def get_upper_by_id(id: int) -> Upper | None:
    """根据ID获取UP主信息

    :param id: UP主ID
    :return: UP主信息
    """
    conn = sqlite3.connect(config.sqlite3_file)
    cursor = conn.cursor()
    upper = cursor.execute('SELECT * FROM upper WHERE id=?', (id,)).fetchone()

    cursor.close()
    conn.close()
    if upper is None:
        return None
    return Upper(upper[0], upper[1], upper[2], upper[3])


def save_upper(id: int, name: str, introduction: str, update_time: int):
    """保存UP主信息，已存在则替换

    """
    conn = sqlite3.connect(config.sqlite3_file)
    cursor = conn.cursor()
    cursor.execute('INSERT OR REPLACE INTO upper VALUES (?, ?, ?, ?)',
                   (id, name, introduction, update_time))
    conn.commit()

    cursor.close()
    conn.close()
