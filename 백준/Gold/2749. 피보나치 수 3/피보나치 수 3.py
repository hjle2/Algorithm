def fibo():
    dp = [0] * (1500000+2)
    dp[1] = 1
    for i in range(1500000):
        dp[i+2] = (dp[i+1] + dp[i]) % INF
    return dp


n = int(input())
INF = 1000000
dp = fibo()
print(dp[n%1500000])