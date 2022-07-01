for _ in range(int(input())):
    K = int(input())
    size = [*map(int, input().split())]
    dp = [[0] * K for _ in range(K)]
    for d in range(1, K):
        for i in range(K-d):
            j = i + d
            dp[i][j] = sum(size[i:j+1]) + min(dp[i][i+k] + dp[i+k+1][j]for k in range(d))
    print(dp[0][-1])