N = int(input())
dp = [0] * (N+1)

for i in range(2, N+1):
    ret = dp[i-1]
    if i%2 == 0:
        ret = min(ret, dp[i//2])
    if i%3 == 0:
        ret = min(ret, dp[i//3])
    dp[i] = ret + 1
print(dp[N])
