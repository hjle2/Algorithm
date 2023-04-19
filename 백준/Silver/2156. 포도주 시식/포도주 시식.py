n = int(input())
wine = [int(input()) for _ in range(n)]

dp = [[0] * 2 for _ in range(n)]

dp[0][0] = wine[0]
ans = 0
if n == 1:
    ans = wine[0]
if n > 1:
    dp[1][0] = wine[1]
    dp[1][1] = wine[0] + wine[1]
    ans = max(dp[1])
if n > 2:
    dp[2][0] = max(dp[0]) + wine[2]
    dp[2][1] = dp[1][0] + wine[2]
    ans = max(ans, max(dp[2]))
for i in range(3, n):
    dp[i][0] = max(max(dp[i-2]), max(dp[i-3])) + wine[i]
    dp[i][1] = dp[i-1][0] + wine[i]
    ans = max(ans, dp[i][0], dp[i][1])
print(ans)

# 6
# 1000
# 1000
# 1
# 1
# 1000
# 1000
# 10
# 977
# 200
# 517
# 851
# 23
# 662
# 880
# 815
# 26
# 214