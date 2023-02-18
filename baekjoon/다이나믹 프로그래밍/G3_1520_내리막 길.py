# 각 칸은 높이가 씌여 있음
# 상하좌우 이웃한 곳 이동 가능
# 세준이는 제일 왼쪽 위에 서 아래 오른쪽으로 이동하려고 한다
## 힘을 덜 들여 높이가 낮은 지점으로만 이동하고 싶음
# 경로의 개수
import sys

sys.setrecursionlimit(10**6)
def dfs(x, y):
    if x == 0 and y == 0:
        return 1
    if dp[x][y] >= 0:
        return dp[x][y]
    dp[x][y] = 0
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0<=nx<N and 0<=ny<M and A[x][y] < A[nx][ny]:
            dp[x][y] += dfs(nx, ny)
    return dp[x][y]

N, M = map(int, input().split())
A = [[*map(int, input().split())]for _ in range(N)]
dp = [[-1] * M for _ in range(N)]
print(dfs(N-1, M-1))