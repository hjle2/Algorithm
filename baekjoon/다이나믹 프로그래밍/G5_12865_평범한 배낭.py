N, K = map(int, input().split())
wv = [[0, 0]] + [[*map(int, input().split())]for _ in range(N)]
dp = [[0] * (N+1)for _ in range(K+1)]
for w in range(1, K+1):
    for i in range(1, N+1):
        if wv[i][0] <= w:
            dp[w][i] = max(dp[w][i-1], dp[w-wv[i][0]][i-1] + wv[i][1])
        else:
            dp[w][i] = dp[w][i-1]
print(dp[-1][-1])