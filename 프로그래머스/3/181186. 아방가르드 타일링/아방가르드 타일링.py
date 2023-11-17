def solution(n):
    mod = 1000000007
    dp = [1, 1, 3, 10, 23, 62]
    
    for i in range(6, n+1):
        dp.append((dp[i-1] + dp[i-2] * 2 + dp[i-3] * 6 + dp[i-4] - dp[i-6]) % mod)
    return dp[n]