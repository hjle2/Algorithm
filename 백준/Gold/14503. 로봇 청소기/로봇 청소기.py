# 로봇 청소기가 청소하는 영역의 개수를 구하여라
# 장소는 N * M 의 직사각형
# 각 칸은 벽, 또는 빈칸
# 청소기는 바라보는 사방향이 있다
# 동작 순서는 다음과 같다
# 1. 현재 위치를 청소한다
# 2. 현재 위치에서 현재 방향을 기준으로 왼쪽부터 차례대로 탐색한다
# 왼쪽 방향에 청소하지 않은 공감이 존재한다면 왼쪽으로 회전한 후 한 칸 전진
# 왼쪽에 청소할 공간이 없다면 그 방향으로 회전 2번으로 돌아간다
# 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진 하고 2번으로 돌아간다
# 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽으로 후진도 할 수 없는 경우에는 작동을 멈춘다
# 0 : 북, 1 : 동, 2 : 남, 3: 서
# 북쪽을 바라보고 있었다면 -> 서쪽
# 서쪽을 바라보고 있었다면 -> 남쪽
# 남쪽을 바라보고 있었다면 -> 동쪽
# 동쪽을 바라보고 있었다면 -> 북쪽

# 북을 보고있으면, 서 남 동 북 순으로 탐색
# 동을 보고있으면, 북 서 남 동 순으로 탐색
# 남을 보고있으면, 동 북 서 남 순으로 탐색
# 서를 보고있으면, 남 동 북 서 순으로 탐색
import sys

input = sys.stdin.readline

def getCnt(r, c, d):
    cnt = 0
    while 1:
        # 청소할 수 있다면 청소한다
        if A[r][c] == 0:
            A[r][c] = -1
            cnt += 1
        canclean = False
        # 4 방향 탐색
        for i in range(1, 5):
            # 현재 방향 기준 왼쪽붵 차례로 탐색
            nd = (d - i) % 4
            # 다음 위치
            nr, nc = r + dr[nd], c + dc[nd]
            # 다음 위치가 청소 가능하다면,
            if 0 <= nr < N and 0 <= nc < M and A[nr][nc] == 0:
                r, c, d = nr, nc, nd
                canclean = True
                break
        # 4 방향 중에 청소 가능한 위치가 없었다면,
        if not canclean:
            # 후진할 좌표
            nr, nc = r - dr[d], c - dc[d]
            # 후진할 수 없는 경우
            if nr < 0 or nr >= N or nc < 0 or nc >= M or A[nr][nc] == 1:
                return cnt
            # 후진 가능한 경우
            else:
                r, c = nr, nc

N, M = map(int, input().split())
r, c, d = map(int, input().split())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
A = [[*map(int, input().split())]for _ in range(N)]
print(getCnt(r, c, d))