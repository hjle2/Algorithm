# 정렬된 두 묶음의 숫자카드가 있다
# 두 묶음을 합쳐 하나로 만드는데 A+B 의 비교를해야한다
# N 개의 숫자 카드 묶음이 있을 때 최소한 몇 번의 비교가 필요한 지 구하라

import sys
import heapq
input = sys.stdin.readline
N = int(input())
card = []
for _ in range(N):
    heapq.heappush(card, int(input()))
cnt = 0
if N == 1:
    print(0)
else:
    while len(card) > 1:
        tmp = heapq.heappop(card) + heapq.heappop(card)
        cnt += tmp
        heapq.heappush(card, tmp)
    print(cnt)
