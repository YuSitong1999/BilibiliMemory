import sys

import file
import aim
import update
import logger

if __name__ == '__main__':
    file.ensure_directory_and_file()
    logger.configure_logger()

    opt = sys.argv[1]
    if opt == 'aim':
        aim.main(sys.argv[2:])
    elif opt == 'update':
        update.main()
    elif opt == 'clear':
        logger.clear(sys.argv[2:])
        exit(0)

    logger.delete_old_log_file()
