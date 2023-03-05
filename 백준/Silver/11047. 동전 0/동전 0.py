n, k = map(int, input().split())
a = [int(input())for _ in range(n)]


ans = 0
for i in range(n-1, -1, -1):
    if a[i] > k: continue

    cnt = k // a[i]
    k -= cnt * a[i]
    ans += cnt
print(ans)