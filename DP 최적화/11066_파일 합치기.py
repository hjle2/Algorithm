# 1. dp
for _ in range(int(input())):
    N = int(input())
    lst = [*map(int, input().split())]
    dp = [[0] * N for _ in range(N)]

    for d in range(1, N):
        for s in range(N-d):
            e = s + d
            if d > 1:
                dp[s][e] = min(dp[s][i] + dp[i+1][e]for i in range(s, e))
            dp[s][e] += sum(lst[s:e+1])
    print(dp[0][-1])


# 2. Knuth
for _ in range(int(input())):
    N = int(input())
    lst = [*map(int, input().split())]
    dp = [[0] * N for _ in range(N+1)]
    ot = [*range(N)]

    for d in range(1, N):
        for s in range(N-d):
            e = s + d
            dp[s][e], ot[s] = min((dp[s][i] + dp[i+1][e], i)for i in range(ot[s], ot[s+1]+1))
            dp[s][e] += sum(lst[s:e+1])
    print(dp[0][-1])
