def isall(x, y, n):
    for i in range(n):
        for j in range(n):
            if A[x+i][y+j] != A[x][y]:
                return False
    return True


def isinmem(x, y, n):
    tmp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[i][j] = A[x+i][y+j]
    if tmp in mem:
        return True
    else:
        mem.add(tmp)
        return False


def init():
    big = max(R, C)
    n = 1
    while n < big:
        n <<= 1
    for i in range(R):
        for j in range(n-C):
            A[i].append(0)
    for i in range(n-R):
        A.append([0]*n)
    return n


def solve(x, y, n):
    if isall(x, y, n):
        if isinmem(x, y, n):
            return 1, 0
        else:
            return 1, 1
    og, ef = 1, 1
    n //= 2
    for dx, dy in D:
        a, b = solve(x + dx*n, y + dy*n, n)
        og, ef = og+a, ef+b
    return og, ef


D = [(0, 0), (0, 1), (1, 0), (1, 1)]
R, C = map(int, input().split())
A = [[*map(int, [*input()])]for _ in range(R)]
N = init()
mem = set()
print(*solve(0, 0, N))
