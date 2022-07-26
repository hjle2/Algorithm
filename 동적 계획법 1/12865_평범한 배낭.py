N, K = map(int, input().split())
wv = [[*map(int, input().split())] for _ in range(N)]
dp = [[0] * (N + 1) for _ in range(K + 1)]
# n번째 까지 담는 경우 중 가치가 더 큰 값

for k in range(1, K + 1):
    for n in range(1, N + 1):
        if wv[n-1][0] <= k:
            dp[k][n] = max(dp[k][n-1], dp[k-wv[n-1][0]][n-1] + wv[n-1][1])
        else:
            dp[k][n] = dp[k][n-1]
print(dp[K][N])