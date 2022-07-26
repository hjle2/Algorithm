A, B = [*input()], [*input()]
len_A, len_B = len(A)+1, len(B)+1
dp = [[0] * len_A for _ in range(len_B)]
# A의 i 까지, B의 j까지 비교했을 때, 가장 긴 것
for i in range(1, len_B):
    for j in range(1, len_A):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + (A[j-1] == B[i-1]))
print(dp[-1][-1])
