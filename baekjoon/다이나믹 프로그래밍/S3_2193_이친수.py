def solve(n):
    if n <= 2:
        return 1
    dp = [0, 2, 3]
    for i in range(2, n-1):
        dp.append(dp[-1] + dp[-2])
    return dp[n-2]

N = int(input())
print(solve(N))
