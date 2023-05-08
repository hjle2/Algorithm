n, k = map(int, input().split())
wv = [[*map(int, input().split())]for _ in range(n)]
wv.sort()

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        w, v = wv[i-1]
        if j >= w: # 훔칠 수 있는 거면,
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])