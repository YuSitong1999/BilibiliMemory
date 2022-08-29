import logging
import os
import time

import file

# 默认保留日志文件个数
default_retain_count: int = 10


def delete_old_log_file(retain_count: int = default_retain_count):
    # 临时目录所有文件
    file_list: list[str] = os.listdir(file.tmp_path)
    # 找出日志文件
    log_file_list: list[str] = []
    for file_name in file_list:
        if len(file_name) == len('2022-08-29_13_22_00.log') and file_name.endswith('.log'):
            log_file_list.append(file_name)
    # 旧日志文件少，无需删除
    now_log_file_count: int = len(log_file_list)
    if now_log_file_count <= retain_count:
        print(f'当前日志文件数 {now_log_file_count} <= {retain_count} 要保留的日志文件数，未执行删除')
        return
    # 执行删除
    print(f'删除 {now_log_file_count - retain_count} 个文件')
    for old_file_name in log_file_list[:now_log_file_count - retain_count]:
        logging.debug(f'deleting file: {old_file_name}')
        os.remove(os.path.join(file.tmp_path, old_file_name))


def configure_logger():
    # Debug级别输出到文件
    log_file_path = os.path.join(file.tmp_path, time.strftime('%Y-%m-%d_%H_%M_%S.log'))
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename=log_file_path,
                        filemode='w'
                        )
    # Info级别输出到屏幕
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console_handler.setFormatter(formatter)
    logging.getLogger('').addHandler(console_handler)


def initialize():
    """
    初始化日志
    :return: None
    """
    delete_old_log_file()
    configure_logger()


def clear(argv: list[str]):
    if len(argv) > 1:
        print(f'参数过多!\n{argv[1:]}')
    elif len(argv) == 0:
        delete_old_log_file()
    else:
        delete_old_log_file(int(argv[0]))
