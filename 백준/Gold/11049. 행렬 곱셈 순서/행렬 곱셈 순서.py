def solve():
    dp = [[0] * n for _ in range(n)]

    for i in range(2, n+1):
        for s in range(n-i+1):
            e = s + i - 1
            dp[s][e] = min(dp[s][k] + dp[k+1][e] + matrix[s][0] * matrix[e][1] * matrix[k][1]
                           for k in range(s, e))
    print(dp[0][-1])


n = int(input())
matrix = [[*map(int, input().split())]for _ in range(n)]
solve()