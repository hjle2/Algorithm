# 3, 5 킬로그램의 설탕봉지가 있다
# 주문 킬로그램에 대해 최대한 적은 봉지의 수
# 불가능 하면 -1 출력

N = int(input())
dp = [1e9] * (N+1)
if N >= 3:
    dp[3] = 1
if N>= 5:
    dp[5] = 1
for i in range(6, N+1):
    dp[i] = min((dp[i-d]+1) if dp[i-d] < 1e9 else 1e9 for d in (3, 5))
print(dp[-1] if dp[-1] < 1e9 else -1)