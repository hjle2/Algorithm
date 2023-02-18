N, M = map(int, input().split())
lst = [0, *sorted(map(int, input().split())), N]
M += 1
dp = [[0]*M for _ in range(M+1)]
ot = [*range(M)]

for d in range(1, M):
    for s in range(M-d):
        e = s + d
        if d > 1:
            dp[s][e], ot[s] = min((dp[s][i] + dp[i+1][e], i)for i in range(ot[s], ot[s+1] + 1))
        dp[s][e] += lst[e+1] - lst[s]
print(dp[0][-1])