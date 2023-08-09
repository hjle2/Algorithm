def dfs(idx, v):
    if idx == m:
        print(*ar)
        return

    for i in range(v, n+1):
        ar[idx] = i
        dfs(idx+1, i)


n, m = map(int, input().split())
ar = [1] * m

for i in range(1, n+1):
    ar[0] = i
    dfs(1, i)