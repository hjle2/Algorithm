# N 개의 정수 숭 '연속된' 몇 개의 수를 선택하여 구할 수 있는 가장 큰 합을 구한다.
# dp[i] 는 0~i-1 의 합 중 큰 수 + lst[i]
# 즉, dp[i] = max(lst[i], dp[i-1]+lst[i])
# dp 중 가장 큰 값이 구간합이 가장 큰 수

N = int(input())
dp = [*map(int, input().split())]
ans = dp[0]
for i in range(1, N):
    dp[i] = max(dp[i], dp[i]+dp[i-1])
    ans = max(ans, dp[i])
print(ans)