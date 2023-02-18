def solve(n):
    dp = [0, 1, 1, 1, 2, 2, 3, 4]
    if n < len(dp):
        return dp[n]
    for i in range(7, n):
        dp.append(dp[-1] + dp[-5])
    return dp[n]

for _ in range(int(input())):
    N = int(input())
    print(solve(N))