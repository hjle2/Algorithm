# 계단은 한 번에 1 or 2계단 씩 오를 수 있다.
# 연속 세 개의 계단을 밟으면 안된다!
# 시작점은 미포함.
# 도착 계단은 밞아야 한다.
N = int(input())
lst = [0] + [int(input())for _ in range(N)]
dp = [[0]*2 for _ in range(N+1)]
dp[1][0] = dp[1][1] = lst[1]
for i in range(2, N+1):
    dp[i][0] = dp[i-1][1] + lst[i]
    dp[i][1] = max(dp[i-2][0], dp[i-2][1]) + lst[i]
print(max(dp[-1]))
