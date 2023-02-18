A, B = [*input()], [*input()]
lenA, lenB = len(A) + 1, len(B) + 1
dp = [[0] * lenA for _ in range(lenB)]
for i in range(1, lenB):
    for j in range(1, lenA):
        v = max(dp[i-1][j], dp[i][j-1])
        if A[j-1] == B[i-1]:
            v = max(v, dp[i-1][j-1] + 1)
        dp[i][j] = v
print(dp[-1][-1])
