# N = int(input())
# lst = [[*map(int, input().split())] for _ in range(N)]
# dp = [[0]*N for _ in range(N+1)]
#
# for d in range(1, N):
#     for s in range(N - d):
#         e = s + d
#         dp[s][e], ot[s] = min((dp[s][s+i] + dp[s+i+1][e] + lst[s][0] * lst[e][1] * lst[s+i][1], i)for i in range(ot[s], ot[e]))
# print(dp[0][-1])

# zip short code 에서 찾음
N = int(input())
dp_size = [0] * (N+1)
dp = [[0]*N for _ in range(N)]
for i in range(N-1):
    dp_size[i] = next(map(int, input().split()))
dp_size[N-1], dp_size[N] = map(int, input().split())

for d in range(1, N):
    for s in range(N - d):
        e = s + d
        size = dp_size[s] * dp_size[e+1]
        dp[s][e] = min(size*s + f + b for s, f, b in zip(dp_size[s+1:e+1], dp[s][s:e], dp[e][s+1:e+1]))
print(dp[0][N-1])