n, k = map(int, input().split())
ar = [*map(int, input().split())]

s = sum(ar[:k])
ans = s
for i in range(1, n-k+1):
    s -= ar[i-1]
    s += ar[i + k - 1]
    ans = max(ans, s)
print(ans)