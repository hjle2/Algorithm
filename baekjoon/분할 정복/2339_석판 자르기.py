def isok(x0, y0, x1, y1):
    s = j = 0
    for x in range(x0, x1):
        for y in range(y0, y1):
            if A[x][y] == 1:
                s += 1
            elif A[x][y] == 2:
                j += 1

    if j == 1 and s == 0:
        return 1
    if s == 0 or j == 0:
        return 0
    return -1


def cancut(x0, y0, x1, y1, n, d):
    if x0 + 1 == x1 or y0 + 1 == y1:
        return 0
    rg = [range(x0, x1), range(y0, y1)][d]
    s = 0
    for i in rg:
        x, y = [n, i][not d], [n, i][d]
        if A[x][y] == 1:
            s += 1
        elif A[x][y] == 2:
            return 0
    return s


def solve(x0, y0, x1, y1, d):
    ok = isok(x0, y0, x1, y1)
    if ok >= 0:
        return ok
    ret, d = 0, not d
    rg = [range(x0, x1), range(y0, y1)][not d]
    for i in rg:
        if cancut(x0, y0, x1, y1, i, d):
            a = solve(x0, y0, [x1, i][d], [i, y1][d], d)
            if a == 0: continue
            b = solve([x0, i+1][d], [i+1, y0][d], x1, y1, d)
            if b == 0: continue
            ret += a * b
    return ret


N = int(input())
A = [[*map(int, input().split())]for _ in range(N)]

ans = solve(0, 0, N, N, 0) + solve(0, 0, N, N, 1)
print(ans if ans > 0 else -1)
