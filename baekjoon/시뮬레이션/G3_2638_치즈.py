import sys
from collections import deque
input = sys.stdin.readline
# 세로, 가로
n, m = map(int, input().split())
cheese = [[*map(int, input().split())]for _ in range(n)]

# 가장자리인 0,0부터 시작해서 치즈가 공기중에 닿은 변의 갯수를 구한다!


def in_range(r, c):
    return 0 <= r < n and 0 <= c < m


def touch_air():
    touch = [[0] * m for _ in range(n)]
    v = [[False] * m for _ in range(n)]
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    que = deque([(0, 0)])
    v[0][0] = True

    while que:
        r, c = que.popleft()

        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if in_range(nr, nc) and not v[nr][nc]:
                if cheese[nr][nc]: # 치즈 칸이면,
                    touch[nr][nc] += 1 # 공기에 닿은 칸의 갯수 증가
                else: # 치즈 없는 칸은 다시 탐색하지 않는다
                    v[nr][nc] = True
                    que.append((nr, nc))
    return touch


def melt(touch):
    melt_cnt = 0
    for r in range(n):
        for c in range(m):
            if touch[r][c] >= 2: # 공기에 닿은 변의 수가 2개 이상이면 치즈는 녹는다
                cheese[r][c] = 0 # 치즈 녹음 처리
                melt_cnt += 1 # 녹은 치즈의 수 카운트
    return melt_cnt


def get_cheese_cnt():
    cnt = 0
    for r in range(n):
        for c in range(m):
            if cheese[r][c]:
                cnt += 1
    return cnt

t = 0
cheese_cnt = get_cheese_cnt()

while cheese_cnt > 0:
    t += 1
    # 두 변 이상의 공기가 닿은 치즈 구하기
    touch = touch_air()
    melt_cnt = melt(touch)
    cheese_cnt -= melt_cnt

print(t)