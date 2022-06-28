# 길이가 N 인 계단 수가 총 몇 개 있는지 구해보자!
# 정답을 1,000,000,000 으로 나눈 나머지를 출력!
N = int(input())
dp = [[0]*10 for _ in range(N+1)]
for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, N+1):
    for j in range(10):
        if j-1 >= 0:
            dp[i][j] += dp[i-1][j-1]
        if j+1 < 10:
            dp[i][j] += dp[i-1][j+1]
print(sum(dp[N])%10**9)

