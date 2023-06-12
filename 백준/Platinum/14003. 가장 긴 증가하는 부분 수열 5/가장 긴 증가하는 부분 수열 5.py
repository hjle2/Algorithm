n = int(input())
ar = [*map(int, input().split())]
dp = [1] * n
LIS = [-1000000001]

for i, num in enumerate(ar):
    if LIS[-1] < num:
        LIS.append(num)
        dp[i] = len(LIS) - 1
    else:
        l, r = 1, len(LIS) - 1
        while l <= r:
            m = (l + r) // 2
            if LIS[m] < num:
                l = m + 1
            else:
                r = m - 1
        LIS[r+1] = num
        dp[i] = r+1


print(len(LIS)-1)
v = max(dp)
ans = []
for i in range(n-1, -1, -1):
    if dp[i] == v:
        ans.append(ar[i])
        v -= 1
ans.reverse()
print(*ans)

