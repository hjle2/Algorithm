# K 개의 가방, 각 가방에 담을 수 있는 최대 무게  Ci
# 가방에는 최대 한 개의 보석
# 상덕이가 훔칠 수 있는 보석의 최대 가격

import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
# 무게, 가격
MV = []
for i in range(N):
    heapq.heappush(MV, [*map(int, input().split())])
# 가방의 최대 무게
C = [int(input())for _ in range(K)]
C.sort()

ans = 0
tmpJ = []
for c in C:
    while MV and c >= MV[0][0]:
        heapq.heappush(tmpJ, -heapq.heappop(MV)[1])
    if tmpJ:
        ans -= heapq.heappop(tmpJ)
    elif not MV:
        break
print(ans)