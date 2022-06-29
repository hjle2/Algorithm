N = int(input())
A = [*map(int, input().split())]
dp = [1] * N
ans = 1
for i in range(1, N):
    for j in range(i-1, -1, -1):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    ans = max(ans, dp[i])
print(ans)