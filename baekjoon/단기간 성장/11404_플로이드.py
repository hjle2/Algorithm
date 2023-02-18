# N개의 도시
# M 개의 버스 노선
# A 에서 B 로 가는데 필요한 최소 비용
import sys
input = sys.stdin.readline
INF = 1e9
N = int(input())
M = int(input())
dp = [[INF] * N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    dp[a-1][b-1] = min(dp[a-1][b-1], c)
for i in range(N):
    dp[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

for i in range(N):
    print(*dp[i], sep=' ')