"""
主模块

通过命令行执行命令
"""
import logging
import sys

import aim
import config
import dao
import update

if __name__ == '__main__':
    # 加载配置
    config.load_config()
    # 确认所需文件存在
    dao.ensure_database_file()

    opt = sys.argv[1]
    if opt == 'aim':
        aim.main(sys.argv[2:])
    elif opt == 'update':
        update.main()
    else:
        logging.error(f'未知命令 {opt}')
