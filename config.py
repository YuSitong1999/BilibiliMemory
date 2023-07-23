"""
配置模块
"""
import logging
import os.path
import time

import json5

config_file: str = 'config.json5'
config_example_file: str = 'config_example.json5'

log_file_path: str
sqlite3_file: str
all_media_path: str


def load_config():
    """加载配置

    读取JSON5配置文件
    """
    # 检查配置文件
    if not os.path.exists(config_file):
        # 不存在时复制示例文件
        with open(config_example_file, 'r', encoding='utf-8') as f:
            with open(config_file, 'w', encoding='utf-8') as f2:
                f2.write(f.read())

    # 读取配置文件
    with open(config_file, 'r', encoding='utf-8') as f:
        config = json5.load(f)
    # 设置配置项常量
    global log_file_path, sqlite3_file, all_media_path
    log_file_path = config['log_file_path']
    sqlite3_file = config['sqlite3_file']
    all_media_path = config['all_media_path']
    print(f'log_file_path: {log_file_path}')
    print(f'sqlite3_file: {sqlite3_file}')
    print(f'all_media_path: {all_media_path}')

    # 级联创建目录
    os.makedirs(log_file_path, exist_ok=True)
    os.makedirs(all_media_path, exist_ok=True)

    configure_logger()


def configure_logger():
    global log_file_path
    # Debug级别输出到文件
    log_file = os.path.join(log_file_path, time.strftime('%Y-%m-%d_%H_%M_%S.log'))
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename=log_file,
                        filemode='w'
                        )
    # Info级别输出到屏幕
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console_handler.setFormatter(formatter)
    logging.getLogger('').addHandler(console_handler)
