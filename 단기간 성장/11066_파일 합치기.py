for _ in range(int(input())):
    K = int(input())
    lst = [*map(int, input().split())]
    dp = [[0]*K for _ in range(K)]

    for i in range(1, K):
        for j in range(K-i):
            if i > 1:
                dp[j][j+i] = min(dp[j][j+n] + dp[j+n+1][j+i]for n in range(i))
            dp[j][j+i] += sum(lst[j:j+i+1])

    print(dp[0][K-1])
