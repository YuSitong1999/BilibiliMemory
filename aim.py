import getopt
import math
import sys
import time

import file

command_aim = '''
    python main.py aim
        status
        add <收藏夹ID1>[,<收藏夹ID2>,...,<收藏夹IDN>] [-t <最早发布时间>] [-l <投稿时长>]
        rm <备份目标收藏夹序号> [备份目标条件序号1,...,备份目标条件序号N]
    '''


def aim_rm(argv: list[str], aims: list[file.Aim]) -> list[file.Aim]:
    if len(argv) != 2:
        print(f'参数个数错误!\n{command_aim}')
        return aims

    aim_fav_number = int(argv[0])
    aim_fav_number -= 1
    if aim_fav_number < 0 or aim_fav_number >= len(aims):
        print(f'目标收藏夹{aim_fav_number}不存在!')
        return aims

    aim_limiters_number_set = set[int]()
    for s in argv[1].split(','):
        if not s.isnumeric():
            print(f'参数{s}错误,已跳过')
            continue
        number = int(s) - 1
        if number < 0 or number >= len(aims[aim_fav_number].limiters):
            print(f'参数{number}超出范围,已跳过')
            continue
        aim_limiters_number_set.add(number)

    aims[aim_fav_number].limiters = [aims[aim_fav_number].limiters[i]
                                     for i in range(len(aims[aim_fav_number].limiters))
                                     if i not in aim_limiters_number_set]
    return aims


def aim_add(argv: list[str], aims: list[file.Aim]) -> list[file.Aim]:
    if len(argv) < 1:
        print(f'参数个数错误!\n{command_aim}')
        return aims

    fav_fid_set = set[int]()
    for s in argv[0].split(','):
        if not s.isnumeric():
            print(f'参数{s}错误,已跳过')
            continue
        fav_fid_set.add(int(s))

    argv = argv[1:]

    try:
        opts, args = getopt.getopt(argv, "a:d:", [])
    except getopt.GetoptError:
        print(f'参数错误{command_aim}')
        sys.exit(1)

    after_timestamp: int = 0
    max_duration: int = 36000
    for opt, arg in opts:
        if opt == '-a':
            after_timestamp = math.floor(time.mktime(time.strptime(arg, '%Y-%m-%d')))
        elif opt == '-d':
            max_duration = int(arg)

    limiter = file.Limiter(after_timestamp, max_duration)
    for i in range(len(aims)):
        if aims[i].fid in fav_fid_set:
            aims[i].limiters.append(limiter)
            fav_fid_set.remove(aims[i].fid)

    for fid in fav_fid_set:
        aims.append(file.Aim(fid, [limiter]))
    return aims


def main(argv: list[str]):
    """
    备份目标
    :param argv:
    :return:
    """

    operation_status = 'status'
    operation_add = 'add'
    operation_rm = 'rm'

    if len(argv) == 0 or argv[0] not in (operation_add, operation_rm, operation_status):
        print(f'命令"{argv}"不受支持，请输入支持的命令:\n{command_aim}')
        return

    operation = argv[0]
    argv = argv[1:]
    aims = file.read_aim_json()

    # 删除备份目标条目
    if operation == operation_rm:
        aims = aim_rm(argv, aims)

    if operation == operation_add:
        aims = aim_add(argv, aims)

    # 查看当前备份目标
    aims_len = len(aims)
    print(aims)
    if aims_len == 0:
        print('查看当前目标收藏夹为空!')
    for i in range(aims_len):
        print(f'{i + 1}: {aims[i]}')

    # 更新备份目标收藏夹
    file.write_aim_json(aims)
