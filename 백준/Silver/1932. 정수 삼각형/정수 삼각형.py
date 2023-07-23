n = int(input())
triangle = []
for _ in range(n):
    tmp = [*map(int, input().split())]
    triangle.append(tmp)

dp = [[0] * (i+1) for i in range(n)]
for i in range(n):
    for j in range(i+1):
        dp[i][j] = triangle[i][j]
        tmp = 0
        if i-1 >= 0:
            if i-1 >= j:
                tmp = dp[i-1][j]
            if j-1 >= 0:
                tmp = max(tmp, dp[i-1][j-1])
        dp[i][j] += tmp
print(max(dp[-1]))