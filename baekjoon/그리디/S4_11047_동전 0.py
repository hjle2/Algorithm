# N개 종류의 동전을 갖고 있다
# 개수는 매우 많이
# 동전을 적절히 사용해 그 동전의 합을 K로 만드려고 한다
# 동전 개수의 최소값을 구하라

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = [int(input())for _ in range(N)]

cnt = 0
for coin in A[::-1]:
    if K >= coin:
        cnt += K // coin
        K = K % coin
print(cnt)