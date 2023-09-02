def solve():
    if n < 2:
        return 1
    dp = [1] * (n+1)
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]


n = int(input())
print(solve())