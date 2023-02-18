N = int(input())
step = [0] * 3 + [int(input())for _ in range(N)]
dp = [0] * (N+3)
for i in range(3, N+3):
    v = dp[i-3] + step[i-1]
    v = max(v, dp[i-2])
    dp[i] = v + step[i]
print(dp[-1])