n = int(input())
a = [int(input()) for _ in range(n)]
a.sort()

ans = 0
for i in range(n):
    tmp = (n-i) * a[i]
    ans = max(ans, tmp)
print(ans)