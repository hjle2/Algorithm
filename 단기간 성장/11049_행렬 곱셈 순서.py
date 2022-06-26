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


# 1. DFS 방식
# def dfs(s, e, cnt):
#     if s == 0 and e == N-1:
#         global ans
#         ans = min(ans, cnt)
#         return
#     if s-1 >= 0:
#         dfs(s-1, e, cnt + rc[s-1][0] * rc[s-1][1] * rc[e][1])
#     if e+1 < N:
#         dfs(s, e+1, cnt + rc[s][0] * rc[e+1][0] * rc[e+1][1])
#
#
# ans = 0
# N = int(input())
# rc = [[*map(int, input().split())]for _ in range(N)]
# for i in range(N-1):
#     dfs(i, i+1, rc[i][0] * rc[i][1] * rc[i+1][1])
# print(ans)
#
