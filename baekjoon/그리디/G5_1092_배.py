# 박스안에 있는 화물을 배에 실어야 한다
# 항구에는 크레인이 N대 있고, 1분에 1개의 박스를 배에 실을 수 있다
# 모든 크레인은 동시에 움직인다
# 크레인에는 무게 제한이 있다
# 모든 박스를 배로 옮기는 데 드는 시간의 최솟값을 구하여라

import sys

input = sys.stdin.readline


def getAns():
    W.sort()
    B.sort()
    if W[-1] < B[-1]:
        return -1

    cnt = [0] * N
    wi = 0
    for bi, b in enumerate(B):
        if b <= W[wi]:
            cnt[wi] += 1
        else:
            while W[wi] < b:
                wi += 1
            cnt[wi] += 1
    t = 0
    total = 0
    while 1:
        t += 1
        for wi, w in enumerate(W):
            if cnt[wi]:
                cnt[wi] -= 1
                total += 1
            else:
                while wi >= 0 and cnt[wi] == 0:
                    wi -= 1
                if wi >= 0:
                    cnt[wi] -= 1
                    total += 1

        if total == M:
            break
    return t

N = int(input())
W = [*map(int, input().split())]
M = int(input())
B = [*map(int, input().split())]

print(getAns())
# 4
# 2 3 5 10
# 17
# 1 1     1 1 1 2 2       4 5 5 5 5          9 9 9 9 9
# -> 6