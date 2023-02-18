N = int(input())
dp = [1, 0, 3, 0]
for i in range(4, N+1):
    if i % 2 == 1:
        dp.append(0)
        continue
    dp.append(dp[i-2] * dp[2])
    for j in range(4, i+1, 2):
        dp[i] += 2 * dp[i-j]
print(dp[N])