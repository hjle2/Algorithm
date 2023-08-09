def dfs(sum, sub, mul, div, val, idx):
    global max_v, min_v
    if idx == n:
        min_v = min(min_v, val)
        max_v = max(max_v, val)
        return

    if sum:
        dfs(sum - 1, sub, mul, div, val + ar[idx], idx + 1)
    if sub:
        dfs(sum, sub - 1, mul, div, val - ar[idx], idx + 1)
    if mul:
        dfs(sum, sub, mul - 1, div, val * ar[idx], idx + 1)
    if div:
        dfs(sum, sub, mul, div - 1, int(val / ar[idx]), idx + 1)


n = int(input())
ar = [*map(int, input().split())]
a, b, c, d = map(int, input().split())
max_v = -1e9
min_v = 1e9
dfs(a, b, c, d, ar[0], 1)
print(int(max_v), int(min_v), sep='\n')
