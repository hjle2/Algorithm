N, K = map(int, input().split())
wv = [[*map(int, input().split())]for _ in range(N)]
# dp[i][j] 는 wv[0~i] 의 물건을 이용하여 k 무게를 만드는 물건의 최대 가치값
dp = [[0] * (N+1)for _ in range(K+1)]

for k in range(1, K+1):
    for n in range(1, N+1):
        # n번째 물건이 k무게 이하여서 담을 수 있을 경우
        if k >= wv[n-1][0]:
            # n번째 물건을 담지 않고, n-1 물건 까지로 k 무게를 만든 경우 혹은
            # n-1 물건 까지로 k-wv[n][0] 즉 n번째 물건을 담을 수 있는 경우의 최대 가치
            dp[k][n] = max(dp[k][n-1], dp[k-wv[n-1][0]][n-1] + wv[n-1][1])
        # n번째 물건을 담을 수 없는 경우
        else:
            # n-1 번째 물건을 담아 k무게를 만드는 경우의 최대 가치
            dp[k][n] = dp[k][n-1]

print(dp[K][N])