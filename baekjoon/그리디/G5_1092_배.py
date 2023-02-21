import sys

input = sys.stdin.readline


def solve():
    if crain[0] < box[0]: # 크레인이 들지 못하는 박스가 있으면 -1
        return -1

    t = 0
    while box:
        t += 1
        for c in crain: # 크레인을 돌면서
            if not box or c < box[-1]: break # 크레인을 계속 탐색한다고 하더라도 옮길 수 있는 박스가 없다면 더 탐색하지 않는다.
            for bi, b in enumerate(box): # 옮길 수 있는 박스를 찾는다
                if c >= b: # 박스를 옮길 수 있따면
                    del box[bi] # 옮길 박스에서 지우고 박스 탐색 그만하기!
                    break
    return t


n = int(input()) # 50
crain = [*map(int, input().split())]
m = int(input()) # 10000
box = [*map(int, input().split())]
crain.sort(reverse=True)
box.sort(reverse=True)

print(solve())