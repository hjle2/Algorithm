RGB = [0, 1, 2]
# 집의 수
N = int(input())
# 집을 칠하는 비용
cost = [[*map(int, input().split())]for _ in range(N)]
dp = [[0]*3 for _ in range(N)]
for i in RGB:
    dp[0][i] = cost[0][i]
for i in range(1, N):
    for j in RGB:
        dp[i][j] = min(dp[i-1][(j-1) % 3], dp[i-1][(j+1) % 3]) + cost[i][j]
print(min(dp[-1]))
