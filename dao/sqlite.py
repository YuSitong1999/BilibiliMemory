"""sqlite

SQLite3 存储模块
"""

import os
import sqlite3

import config


def ensure_database_file():
    """确认数据库文件存在

    数据库文件不存在时创建
    """
    # 检查数据库文件是否存在
    if not os.path.exists(config.sqlite3_file):
        create_new_database_and_table()


def create_new_database_and_table():
    """创建新数据库和表

    删除配置路径下的旧数据库文件，创建新数据库文件和数据表
    """

    # 删除已存在的数据库文件
    if os.path.exists(config.sqlite3_file):
        os.remove(config.sqlite3_file)

    # 创建和连接新数据库
    conn = sqlite3.connect(config.sqlite3_file)
    cursor = conn.cursor()
    # 创建UP主信息表(upper)
    cursor.execute('''CREATE TABLE upper(
    id INT PRIMARY KEY,
    name TEXT NOT NULL,
    introduction TEXT NOT NULL,
    update_time INT NOT NULL
    )''')
    # 创建投稿信息表(media)
    cursor.execute('''CREATE TABLE media(
    bv_id CHAR(12) PRIMARY KEY,
    up_id INT NOT NULL,
    title TEXT NOT NULL,
    introduction TEXT NOT NULL,
    duration INT NOT NULL,
    create_time INT NOT NULL,
    favorite_time INT NOT NULL,
    update_time INT NOT NULL,
    is_local BOOL NOT NULL,
    is_delete  NOT NULL,
    FOREIGN KEY(up_id) REFERENCES upper(id)
    )''')
    # 创建投稿所属目标表 (media_aim)
    cursor.execute('''CREATE TABLE media_aim(
    bv_id CHAR(12) NOT NULL,
    aim_id INT NOT NULL,
    PRIMARY KEY(bv_id, aim_id),
    FOREIGN KEY(bv_id) REFERENCES media(bv_id),
    FOREIGN KEY(aim_id) REFERENCES aim(id)
    )''')
    # 创建下载目标表(aim)
    cursor.execute('''CREATE TABLE aim(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type INT NOT NULL,
    target_id INT NOT NULL,
    name TEXT NOT NULL,
    update_time INT NOT NULL,
    UNIQUE(type, target_id)
    )''')
    # 创建目标限制表(aim_limiter)
    cursor.execute('''CREATE TABLE aim_limiter(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aim_id INT NOT NULL,
    after INT,
    max_duration INT,
    FOREIGN KEY(aim_id) REFERENCES aim(id) 
    )''')
    conn.commit()

# def aim_limiter_from_record(record: tuple) -> AimLimiter:
#     return AimLimiter(record[0], record[1], record[2], record[3])
#
#
# def aim_from_record(aim_record: tuple, aim_limiters_record: list[tuple] | None) -> Aim:
#     return Aim(aim_record[0], aim_record[1], aim_record[2], aim_record[3], aim_record[4],
#                [aim_limiter_from_record(aim_limiter_record) for aim_limiter_record in aim_limiters_record]
#                if aim_limiters_record is not None else None)
#
#
# def connect_sqlite3_and_do(f) -> any:
#     conn = sqlite3.connect(os.path.join(file.meta_path, 'sqlite3.db'))
#     cursor = conn.cursor()
#     result: any = f(cursor)
#     cursor.close()
#     conn.close()
#     return result
#
#
# def read_all_type_aim() -> [list[Aim], list[Aim]]:
#     def f(cursor: sqlite3.Cursor):
#         aim_records: list[tuple] = cursor.execute('SELECT * FROM aim', ).fetchall()
#         aim_favorites = list[Aim]()
#         aim_upper = list[Aim]()
#         for aim_record in aim_records:
#             now_aim = Aim(aim_record)
#             if now_aim.type == aim.AIM_FAVORITE_TYPE_ID:
#                 aim_favorites.append(now_aim)
#             else:
#                 aim_upper.append(now_aim)
#         return aim_favorites, aim_upper
#
#     return connect_sqlite3_and_do(f)
#
#
# def get_aim(type: int, target_id: int) -> Aim:
#     def f(cursor: sqlite3.Cursor):
#         aim_record: tuple | None = cursor.execute('SELECT * FROM aim WHERE type=? AND target_id=?',
#                                                   (type, target_id)).fetchone()
#         return aim_from_record(aim_record, None)
#
#     return connect_sqlite3_and_do(f)
#
#
# def create_aim(aim: Aim) -> int:
#     pass
#
#
# def update_aim_record(now_aim: Aim):
#     pass
#
#
# def delete_aim_record(id: int):
#     pass
