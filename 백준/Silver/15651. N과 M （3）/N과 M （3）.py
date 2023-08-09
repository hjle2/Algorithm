def dfs(idx):
    if idx == m:
        print(*ar)
        return

    for i in range(1, n+1):
        ar[idx] = i
        dfs(idx+1)


n, m = map(int, input().split())
ar = [1] * m

for i in range(1, n+1):
    ar[0] = i
    dfs(1)