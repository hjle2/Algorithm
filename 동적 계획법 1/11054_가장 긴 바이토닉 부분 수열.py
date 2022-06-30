N = int(input())
A = [*map(int, input().split())]
dp = [1] * N
dp1 = [0] * N
for i in range(1, N):
    for j in range(i-1, -1, -1):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

for i in range(N-2, -1, -1):
    for j in range(i+1, N):
        if A[i] > A[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)

print(max(dp[i] + dp1[i]for i in range(N)))

