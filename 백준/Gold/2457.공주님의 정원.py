import sys
input = sys.stdin.readline
n = int(input())
flower = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    flower.append((a * 100 + b, c * 100 + d))
flower.sort(key=lambda x:(x[0], x[1]))


def solve():
    nxt_end = 0
    cur_end = 301
    flowerCnt = 0
    if flower[0][0] > cur_end:
        return 0

    for s, e in flower:
        # start_day를 갱신하는 조건
        if s > cur_end:
            flowerCnt += 1
            cur_end = nxt_end
        # end_day를 갱신하는 조건 지금 피있는 꽃과 이어져 피는 경우
        if s <= cur_end and nxt_end < e:
            nxt_end = e

        if nxt_end > 1130:
            cur_end = nxt_end
            flowerCnt += 1
            break

    if cur_end <= 1130:
        flowerCnt = 0

    return flowerCnt


print(solve())
