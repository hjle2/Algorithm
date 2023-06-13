n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

ans = 0
for i in range(n-1, -1, -1):
    if k < a[i]: continue
    tmp = k // a[i]
    ans += tmp
    k -= tmp * a[i]
print(ans)