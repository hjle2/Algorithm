n = int(input())
ar = [int(input()) for _ in range(n)]
dp1 = [0] * n
dp2 = [0] * n
for i in range(n):
    if i-1 >= 0:
        dp1[i] = dp2[i-1]
    if i-2 >= 0:
        dp2[i] = max(dp1[i-2], dp2[i-2])
    dp1[i] += ar[i]
    dp2[i] += ar[i]
print(max(dp1[-1], dp2[-1]))
