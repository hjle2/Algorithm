N, K = map(int, input())
wv = [[0] + [*map(int, input().split())]for _ in range(N)]
dp = [[0]*(N+1)for _ in range(K+1)]
# dp[k][n] = 무게 k 까지의 1번째 ~ n번쨰 물건을 넣었을 때의 최대 가치

for k in range(1, K+1):
    for n in range(1, N+1):
        if k < wv[n]:
            dp[k][n] = max(dp[k][n-1], dp[k-wv[n][0][n] + wv[n][0]])
        else:
            dp[k][n] = dp[k][n-1]
print(dp[-1][-1])
