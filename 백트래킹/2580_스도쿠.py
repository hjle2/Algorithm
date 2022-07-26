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


def dfs(n):
    if n == len(lst):
        return True
    r, c = lst[n]
    for v in range(1, N+1):
        if ispossible(r, c, v):
            ar[r][c] = v
            if dfs(n+1): return True
            ar[r][c] = 0
    return False


N = 9
ar = [[*map(int, input().split())]for _ in range(N)]
lst = []
for i in range(N):
    for j in range(N):
        if ar[i][j] == 0:
            lst.append((i, j))
dfs(0)

for i in range(N):
    print(*ar[i])