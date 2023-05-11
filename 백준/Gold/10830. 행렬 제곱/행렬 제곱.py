def multiple(a, b):
    ret = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp = 0
            for k in range(n):
                tmp += a[i][k] * b[k][j] % 1000
            ret[i][j] = tmp % 1000
    return ret


def power(base, exp):
    if exp == 1:
        ret = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ret[i][j] = base[i][j] % 1000
        return ret

    tmp = power(base, exp//2)

    if exp % 2 == 1:
        return multiple(multiple(tmp, tmp), base)
    else:
        return multiple(tmp, tmp)


n, b = map(int, input().split())
a = [[*map(int, input().split())] for _ in range(n)]

ret = power(a, b)
for i in range(n):
    print(*ret[i], sep=' ')

