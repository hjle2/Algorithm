def ispossible(r, c, v):
    for i in range(N):
        if ar[r][i] == v or ar[i][c] == v:
            return False

    r, c = r // 3 * 3, c // 3 * 3
    for i in range(3):
        for j in range(3):
            if ar[r+i][c+j] == v:
                return False
    return True


def possiblecases(r, c):
    ret = []
    for v in range(1, N+1):
        if ispossible(r, c, v):
            ret.append(v)
    return ret

def dfs(n):
    if n == len(dic):
        return True
    r, c = key_list[n]
    for v in dic[(r, c)]:
        if ispossible(r, c, v):
            ar[r][c] = v
            if dfs(n+1): return True
            ar[r][c] = 0
    return False


N = 9
ar = [[*map(int, input().split())]for _ in range(N)]
lst = []
dic = {}
key_list = list(dic.keys())
for i in range(N):
    for j in range(N):
        if ar[i][j] == 0:
            dic[(i, j)] = possiblecases(i, j)
            # lst.append((i, j))

key_list = list(dic.keys())
dfs(0)

for i in range(N):
    print(*ar[i])

# 0 0 0 0 0 0 0 0 1
# 0 0 0 0 0 0 0 0 2
# 0 0 0 0 0 0 0 0 3
# 0 0 0 0 0 0 0 0 4
# 0 0 0 0 0 0 0 0 5
# 0 0 0 0 0 0 0 0 6
# 0 0 0 0 0 0 0 0 7
# 0 0 0 0 0 0 0 0 8
# 0 0 0 0 0 0 0 0 9
