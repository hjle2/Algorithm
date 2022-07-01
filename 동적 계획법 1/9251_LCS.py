A, B = [*input()], [*input()]
len_A, len_B = len(A)+1, len(B)+1
dp = [[0] * len_A for _ in range(len_B)]
for i in range(1, len_B):
    for j in range(1, len_A):
        # !!
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + (A[j-1] == B[i-1]))
print(dp[len_B-1][len_A-1])
