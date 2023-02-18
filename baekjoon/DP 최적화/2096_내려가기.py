import sys
from copy import deepcopy

input = sys.stdin.readline
N, K = int(input()), 3

minDp = [*map(int, input().split())]
maxDp = deepcopy(minDp)
minTmp, maxTmp = [0] * 3, [0] * 3

for i in range(1, N):
    ar = [*map(int, input().split())]
    for j in range(K):
        minTmp[j] = minDp[j]
        maxTmp[j] = maxDp[j]
        if j-1 >= 0:
            minTmp[j] = min(minTmp[j], minDp[j-1])
            maxTmp[j] = max(maxTmp[j], maxDp[j-1])
        if j+1 < K:
            minTmp[j] = min(minTmp[j], minDp[j+1])
            maxTmp[j] = max(maxTmp[j], maxDp[j+1])

    for j in range(K):
        minDp[j] = minTmp[j] + ar[j]
        maxDp[j] = maxTmp[j] + ar[j]
print(max(maxDp), min(minDp))