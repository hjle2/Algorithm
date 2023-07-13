n = int(input())

dp = [0] * 3
prv = [0] * 3

for _ in range(n):
    a, b, c = map(int, input().split())
    for i in range(3):
        if i == 0:
            dp[i] = min(prv[1], prv[2]) + a
        elif i == 1:
            dp[i] = min(prv[0], prv[2]) + b
        else:
            dp[i] = min(prv[0], prv[1]) + c
    prv = dp[:]
print(min(dp))