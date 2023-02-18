N = int(input())
TP = [[0, 0]] + [[*map(int, input().split())]for _ in range(N)]
dp = [0] * (N+1)
for i in range(1, N+1):
    t, p = TP[i]
    dp[i] = max(dp[i], dp[i-1])
    if t + i -1 <= N:
        dp[t+i-1] = max(dp[t+i-1], dp[i-1]+p)
print(dp[-1])