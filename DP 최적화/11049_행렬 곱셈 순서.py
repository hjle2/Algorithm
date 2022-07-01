N = int(input())
lst = [[*map(int, input().split())] for _ in range(N)]
dp = [[0]*N for _ in range(N+1)]
ot = [*range(N)]

for d in range(1, N):
    for s in range(N - d):
        e = s + d
        dp[s][e], ot[s] = min((dp[s][s+i] + dp[s+i+1][e] + lst[s][0] * lst[e][1] * lst[s+i][1], i)for i in range(ot[s], ot[e]))
print(dp[0][-1])