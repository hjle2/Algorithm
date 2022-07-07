def init():
    big = max(R, C)
    n = 1
    while n < big:
        n <<= 1
    if n-R > 0:
        for i in range(R):
            for _ in range(n-C):
                A[i].append(0)
    for _ in range(n-R):
        A.append([0] * n)
    return n


def isall(x, y, n):
    for r in range(n):
        for c in range(n):
            if A[x+r][y+c] != A[x][y]:
                return False
    return True


def solve(x, y, n):
    if isall(x, y, n):
        return 1
    if n == 2:
        return 4
    ret = 1
    for dx, dy in d:
        nx, ny = x + dx*n, y + dy*n
        ret += solve(x, y, n // 2)
    return ret

d = [(0, 0), (0, 1), (1, 0), (1, 1)]
R, C = map(int, input().split())
A = [[*input()]for _ in range(R)]
N = init()
print(solve(0, 0, N))
