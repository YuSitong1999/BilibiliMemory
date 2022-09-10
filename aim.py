import getopt
import logging
import math
import sys
import time

import file

command_aim = '''
    python main.py aim
        status
        add <收藏夹ID1>[,<收藏夹ID2>,...,<收藏夹IDN>] [-t <最早发布时间>] [-l <投稿时长>]
        rm <备份目标收藏夹序号> [备份目标条件序号1,...,备份目标条件序号N]
        addm <投稿BV ID1>[,<投稿BV ID2>,...,<投稿BV IDN>]
        rmm <投稿BV ID1>[,<投稿BV ID2>,...,<投稿BV IDN>]
    '''


def aim_rm_favorites(argv: list[str], aim_favorites: list[file.Aim]) -> list[file.Aim]:
    if len(argv) != 2:
        print(f'参数个数错误!\n{command_aim}')
        return aim_favorites

    aim_fav_number = int(argv[0])
    aim_fav_number -= 1
    if aim_fav_number < 0 or aim_fav_number >= len(aim_favorites):
        print(f'目标收藏夹{aim_fav_number}不存在!')
        return aim_favorites

    aim_limiters_number_set = set[int]()
    for s in argv[1].split(','):
        if not s.isnumeric():
            print(f'参数{s}错误,已跳过')
            continue
        number = int(s) - 1
        if number < 0 or number >= len(aim_favorites[aim_fav_number].limiters):
            print(f'参数{number}超出范围,已跳过')
            continue
        aim_limiters_number_set.add(number)

    aim_favorites[aim_fav_number].limiters = [aim_favorites[aim_fav_number].limiters[i]
                                              for i in range(len(aim_favorites[aim_fav_number].limiters))
                                              if i not in aim_limiters_number_set]
    return aim_favorites


def aim_add_favorites(argv: list[str], aim_favorites: list[file.Aim]) -> list[file.Aim]:
    if len(argv) < 1:
        print(f'参数个数错误!\n{command_aim}')
        return aim_favorites

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
    max_duration: int = 0  # 缺省不限制投稿时长
    for opt, arg in opts:
        if opt == '-a':
            after_timestamp = math.floor(time.mktime(time.strptime(arg, '%Y-%m-%d')))
        elif opt == '-d':
            max_duration = int(arg)

    limiter = file.Limiter(after_timestamp, max_duration)
    for i in range(len(aim_favorites)):
        if aim_favorites[i].fid in fav_fid_set:
            aim_favorites[i].limiters.append(limiter)
            fav_fid_set.remove(aim_favorites[i].fid)

    for fid in fav_fid_set:
        aim_favorites.append(file.Aim(fid, [limiter]))
    return aim_favorites


def aim_rm_media(argv: list[str], aim_medias: list[file.AimMedia]) -> list[file.AimMedia]:
    """移除部分目标投稿

    :param argv: 移除目标投稿的bv id集
    :param aim_medias: 原目标投稿
    :return: 新目标投稿
    """
    if len(argv) != 1:
        print(f'参数个数错误!\n{command_aim}')
        return aim_medias

    bv_id_set = set[str]([bv_id.strip() for bv_id in argv[0].split(',')
                          if bv_id.startswith('BV') and len(bv_id) == 12])
    logging.info(f'移除的目标投稿: {bv_id_set}')
    return [aim for aim in aim_medias if aim.bv_id not in bv_id_set]


def aim_add_media(argv: list[str], aim_medias: list[file.AimMedia]) -> list[file.AimMedia]:
    """新增部分目标投稿，格式错误或已存在则跳过

    :param argv: 新增目标投稿的bv id集
    :param aim_medias: 原目标投稿
    :return: 新目标投稿
    """
    if len(argv) != 1:
        print(f'参数个数错误!\n{command_aim}')
        return aim_medias

    bv_id_list = set[str]([aim.bv_id for aim in aim_medias])
    for bv_id in argv[0].split(','):
        if not (bv_id.startswith('BV') and len(bv_id) == 12):
            print(f'bv id {bv_id} 格式错误,已跳过')
            continue
        if bv_id in bv_id_list:
            print(f'bv id {bv_id} 已存在,已跳过')
            continue
        aim_medias.append(file.AimMedia(bv_id))
    return aim_medias


def main(argv: list[str]):
    """
    备份目标
    :param argv:
    :return:
    """

    operation_status = 'status'
    operation_add = 'add'
    operation_rm = 'rm'
    operation_add_media = 'addm'
    operation_rm_media = 'rmm'

    operations = (operation_add, operation_rm, operation_status, operation_add_media, operation_rm_media)
    if len(argv) == 0 or argv[0] not in operations:
        print(f'命令"{argv}"不受支持，请输入支持的命令:\n{command_aim}')
        return

    operation = argv[0]
    argv = argv[1:]
    aim_favorites, aim_medias = file.read_aim_json()

    if operation == operation_rm:
        # 删除备份目标收藏夹
        aim_favorites = aim_rm_favorites(argv, aim_favorites)
    elif operation == operation_add:
        # 新增备份目标收藏夹
        aim_favorites = aim_add_favorites(argv, aim_favorites)
    elif operation == operation_rm_media:
        # 删除目标投稿
        aim_medias = aim_rm_media(argv, aim_medias)
    elif operation == operation_add_media:
        # 新增目标投稿
        aim_medias = aim_add_media(argv, aim_medias)

    # 查看当前备份目标
    aim_favorites_len = len(aim_favorites)
    print(aim_favorites)
    if aim_favorites_len == 0:
        print('查看当前目标收藏夹为空!')
    for i in range(aim_favorites_len):
        print(f'{i + 1}: {aim_favorites[i]}')

    aim_medias_len = len(aim_medias)
    print(aim_medias_len)
    if aim_medias_len == 0:
        print('查看当前目标投稿为空!')
    for i in range(aim_medias_len):
        print(f'{i + 1}: {aim_medias[i]}')

    # 更新备份目标收藏夹
    file.write_aim_json(aim_favorites, aim_medias)
