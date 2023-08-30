N = int(input())
ar = [[*map(int, input().split())]for _ in range(N)]
dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    if i + ar[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], ar[i][1] + dp[i + ar[i][0]])
print(dp[0])