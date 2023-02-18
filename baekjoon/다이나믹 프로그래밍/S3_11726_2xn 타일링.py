n = int(input()) + 1
dp = [0] * n
dp[1] = 1
if n > 2:
    dp[2] = 2
for i in range(3, n):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007
print(dp[-1])