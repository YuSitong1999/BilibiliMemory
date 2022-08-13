import logging
import os
import sys
import time

import file
import aim
import update


def set_log():
    """
    配置日志
    :return: None
    """
    log_file_path = os.path.join(file.tmp_path, time.strftime('%Y-%m-%d_%H_%M_%S.log'))
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename=log_file_path,
                        filemode='w'
                        )
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console_handler.setFormatter(formatter)
    logging.getLogger('').addHandler(console_handler)


if __name__ == '__main__':
    file.ensure_directory_and_file()
    set_log()

    opt = sys.argv[1]
    if opt == 'aim':
        aim.main(sys.argv[2:])
    elif opt == 'update':
        update.main()
