# N 게임에 참여하는 사람 수
# K 게임 시작자가 정한 수
from copy import deepcopy

N, K, M = map(int, input().split())
dp = [[*map(int, input().split())]for _ in range(N)]


for _ in range(K-1):
    tmp = [[]for _ in range(N)]
    for i in range(N):
        for j in dp[i]:
            for k in dp[j-1]:
                if k not in tmp[i]:
                    tmp[i].append(k)
    dp = deepcopy(tmp)

for _ in range(M):
    a, b = map(int, input().split())
    print(['life', 'death'][b in dp[a-1]])
