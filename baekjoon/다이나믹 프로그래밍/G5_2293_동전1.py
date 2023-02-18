N, K = map(int, input().split())
coin = [int(input())for _ in range(N)]
dp = [0] * (K+1)
dp[0] = 1
for i in range(N):
    for j in range(1, K+1):
        if j >= coin[i]:
            dp[j] += dp[j-coin[i]]
print(dp[-1])