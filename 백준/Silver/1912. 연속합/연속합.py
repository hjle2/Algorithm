n = int(input())
ar = [*map(int, input().split())]
dp = [0] * n
dp[0] = ar[0]

for i in range(1, n):
    dp[i] = max(dp[i - 1] + ar[i], ar[i])
print(max(dp))