# ATM 1 대에 N 명이 줄을 서 있다
# i 번 사람이 돈을 인출하는데 걸리는 시간으 Pi분 이다
# 줄을 서는 순서에 따라 시간의 합이 달라진다
# 모든 사람이 돈을 인출하는데 필요한 시간의 최솟값을 구하라

import sys
input = sys.stdin.readline
N = int(input())
P = [*map(int, input().split())]
P.sort()
sum = 0
before = 0
for pi in P:
    sum += before + pi
    before += pi
print(sum)