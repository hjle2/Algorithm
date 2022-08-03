# V개의 마을과 E 개의 일방통행 도로
# 다시 시작점으로 돌아오는 길이가 최소인

INF = 1e9
N, M = map(int, input().split())
dp = [[INF] * N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    dp[a-1][b-1] = c

for i in range(N):
    for j in range(N):
        for k in range(N):
            dp[j][k] = min(dp[j][k], dp[j][i] + dp[i][k])

ans = min(dp[i][i] for i in range(N))
print(ans if ans < INF else -1)
