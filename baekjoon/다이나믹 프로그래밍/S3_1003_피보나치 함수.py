def solve():
    n = int(input()) + 1
    dp = [[0, 0]] * n
    dp[0] = [1, 0]
    if n > 1:
        dp[1] = [0, 1]
    for i in range(2, n):
        dp[i] = dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]
    print(*dp[n-1], sep=' ')

for _ in range(int(input())):
    solve()