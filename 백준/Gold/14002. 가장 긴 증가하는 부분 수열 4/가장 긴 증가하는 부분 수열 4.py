n = int(input())
ar = [*map(int, input().split())]
dp = [1] * n

for i in range(n):
    for j in range(i):
        if ar[i] > ar[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
v = max(dp)
ans = []
for i in range(n-1, -1, -1):
    if v == dp[i]:
        ans.append(ar[i])
        v -= 1
ans.reverse()
print(*ans)