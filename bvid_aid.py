# Bilibili: bv_id to aid
# https://www.zhihu.com/question/381784377/answer/1099438784

table: str = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
tr: dict[str, int] = {}
for i in range(58):
    tr[table[i]] = i
s: list[int] = [11, 10, 3, 8, 4, 6]
xor: int = 177451812
add: int = 8728348608


def bv_id_to_aid(bv_id: str) -> int:
    r: int = 0
    for i in range(6):
        r += tr[bv_id[s[i]]] * 58 ** i
    return (r - add) ^ xor


def aid_to_bv_id(aid: int) -> str:
    aid = (aid ^ xor) + add
    r = list('BV1  4 1 7  ')
    for i in range(6):
        r[s[i]] = table[aid // 58 ** i % 58]
    return ''.join(r)
