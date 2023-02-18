def isall(pt, n):
    x, y = pt
    v = A[x][y]
    for i in range(n):
        nx = x + i
        for j in range(n):
            ny = y + j
            if A[nx][ny] != v:
                return -1
    return v


def solve(pt, n):
    ret = [0, 0]
    v = isall(pt, n)
    if v >= 0:
        ret[v] += 1
        return ret
    x, y = pt
    n = n >> 1
    for dx, dy in d:
        a, b = solve((x + dx*n, y + dy*n), n)
        ret[0] += a
        ret[1] += b
    return ret


d = [(0, 0), (1, 0), (0, 1), (1, 1)]
N = int(input())
A = [[*map(int, input().split())]for _ in range(N)]
print(*solve((0, 0), N), sep='\n')