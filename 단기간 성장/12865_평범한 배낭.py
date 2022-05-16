def solution():
    for i in range(1, n+1):
        for j in range(1, k+1):
            if j >= wv[i-1][0]:
                DP[i][j] = max(DP[i-1][j], DP[i-1][j-wv[i-1][0]] + wv[i-1][1])
            else:
                DP[i][j] = DP[i-1][j]
    return DP[n][k]


n, k = map(int, input().split())
wv = [list(map(int, input().split()))for _ in range(n)]
DP = [[0]*(k+1) for _ in range(n+1)]

print(solution())