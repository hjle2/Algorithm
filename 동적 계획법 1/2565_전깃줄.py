# 전깃 줄의 갯수 0 < N <= 100
N = int(input())
pair = [[*map(int, input().split())]for _ in range(N)]
dp = [1] * N
# pair 를 x[0] 기준으로 정렬한 후
# 가장 긴 증가하는 부분 수열을 구한다.

pair.sort(key=lambda x:x[0])
ans = 0
for i in range(N):
    for j in range(i-1, -1, -1):
        if pair[i][1] > pair[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
    ans = max(ans, dp[i])
print(N - ans)