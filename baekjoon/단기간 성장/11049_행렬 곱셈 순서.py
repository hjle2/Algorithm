def solve(s, e):
    if s == e:
        return 0
    if dp[s][e]:
        return dp[s][e]
    if s+1 == e:
        dp[s][e] = rc[s][0] * rc[s][1] * rc[e][1]
        return dp[s][e]
    for i in range(s, e):
        ret = solve(s, i) + solve(i+1, e) + rc[s][0] * rc[i][1] * rc[e][1]
        if not dp[s][e] or ret < dp[s][e]:
            dp[s][e] = ret
    return dp[s][e]


N = int(input())
rc = [[*map(int, input().split())]for _ in range(N)]
dp = [[0]*N for _ in range(N)]
print(solve(0, N-1))