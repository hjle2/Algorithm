def solve():
    n = int(input()) + 1
    dp = [0] * n
    dp[1] = 1
    if n > 2:
        dp[2] = 2
    if n > 3:
        dp[3] = 4
    for i in range(4, n):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n-1])

for _ in range(int(input())):
    solve()