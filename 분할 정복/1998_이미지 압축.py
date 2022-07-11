def hashFunc(str):
    ret = 0
    for i in range(len(str)):
        ret = (ret * 32741 + ord(str[i])) % 1e9+7
    return ret


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
    allsame = True
    tmp = []
    for i in range(n):
        for j in range(n):
            tmp.append(A[x+i][y+j])
            if A[x][y] != A[x + i][y + j]:
                allsame = False

    if allsame:
        isleaf[x][y][n] = 1
        qStr[x][y][n] = "W" if A[x][y] else "B"
        return 1

    ret = 1
    s = n//2
    for dx, dy in D:
        ret += solve(x + dx * s, y + dy * s, s)
        qStr[x][y][n] += (qStr[x+dx*s][y+dy*s][s])
    return ret


def eff(x, y, n):
    if isleaf[x][y][n]:
        return 1
    if hashFunc(qStr[x][y][n]) in mp.keys():
        return 0
    mp[hashFunc(qStr[x][y][n])] = 1

    ret = 1
    s = n//2
    for dx, dy in D:
        ret += eff(x + dx*s, y + dy*s, s)
    return ret


D = [(0, 0), (0, 1), (1, 0), (1, 1)]
R, C = map(int, input().split())
A = [[*map(int, [*input()])]for _ in range(R)]
mp = dict()
N = init()
isleaf = [[[0]*(N+1) for _ in range(N)]for _ in range(N)]
qStr = [[["X"]*(N+1) for _ in range(N)]for _ in range(N)]
ans = [0, 0]
ans[0] = solve(0, 0, N)
ans[1] = eff(0, 0, N)
print(*ans)