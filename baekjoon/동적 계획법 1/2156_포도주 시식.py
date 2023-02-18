# 선택한 포도주는 다 마시고, 원래 위치에 놓는다.
# 3잔을 연속으로 선택할 수 없다.

N = int(input())
lst = [0] + [int(input())for _ in range(N)]
dp = [[0] * 3 for _ in range(N+1)]
dp[1][1] = dp[1][2] = lst[1]
for i in range(2, N+1):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = dp[i-1][0] + lst[i]
    dp[i][2] = dp[i-1][1] + lst[i]
print(max(dp[N]))
