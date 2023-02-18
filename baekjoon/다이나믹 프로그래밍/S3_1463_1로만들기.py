# X가 3으로 나누어 떨어지면, 나눈다
# X가 2로 나누어 떨어지면, 나눈다
# 1을 뺀다
# 연산의 최소 횟수

N = int(input())
dp = [0] * (N+1)
for i in range(2, N+1):
    v = dp[i-1]
    if i%2 == 0:
        v = min(v, dp[i//2])
    if i%3 == 0:
        v = min(v, dp[i//3])
    dp[i] = v + 1
print(dp[N] if N > 1 else 0)