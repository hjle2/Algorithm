def percent(x, y):
    return y*100//x


def solve():
    if z >= 99:
        return -1
    l, r = 0, 10000000000000
    while l <= r:
        m = (l + r) // 2
        if percent(x + m, y + m) != z:
            ret = m
            r = m - 1
        else:
            l = m + 1
    return ret


x, y = map(int, input().split())
z = percent(x, y)
print(solve())