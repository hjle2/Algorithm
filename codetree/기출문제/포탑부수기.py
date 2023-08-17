# 가장 약한 포탑이 공격자 -> N+M 만큼의 공격력 증가
# 약한 포탑이 여러개라면 가장 최근 공격한 포탑이 약한 포탑
# 그러한 포탑이 여러개라면 행과 열의 합이 가장 큰 포탑이 가장 약한 포탑
# 또 그러한 포탑이 2개 이상이면 포탑 위치의 열 값이 가장 큰 포탑이 약한 포탑

# 가장 강한 포탑을 공격
# 공격력이 가장 높은 포탑
# 공격한 지 가장 오래된 포탑
# 행과 열의 합이 가장 작은 포탑
# 열 값이 가장 작은 포탑
import sys
from collections import deque

input = sys.stdin.readline


def end():
    ret = 0
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                ret += 1
                if ret > 1: return False
    if ret <= 1:
        return True
    else:
        return False


def weak_tower():
    ret = []
    min_power = 1e9
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                if board[i][j] < min_power:
                    min_power = board[i][j]
                    ret = [(i, j)]
                elif board[i][j] == min_power:
                    ret.append((i, j))
    nxt_ret = []
    max_attack = 0
    if len(ret) > 1:        # 가장 약한 파워를 가진 포탑이 여러 개인 경우
        for i, j in ret:
            if attack[i][j] > max_attack:
                max_attack = attack[i][j]
                nxt_ret = [(i, j)]
            elif attack[i][j] == max_attack:
                nxt_ret.append((i, j))
    else:
        return ret[0]

    ret = []
    max_row_col = 0
    if len(nxt_ret) > 1:    # 가장 약한 파워를 가진 포탑 중 최근 공격한 포탑이 여러 개인 경우
        for i, j in nxt_ret:
            if i + j > max_row_col:
                max_row_col = i + j
                ret = [(i, j)]
            elif i + j == max_row_col:
                ret.append((i, j))
    else:
        return nxt_ret[0]

    nxt_ret = []
    min_row = 1e9
    if len(ret) > 1:
        for i, j in ret:
            if i < min_row:
                min_row = i
                nxt_ret = i, j
        return nxt_ret
    else:
        return ret[0]


def strong_tower():
    ret = []
    max_power = 0
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                if board[i][j] > max_power:
                    max_power = board[i][j]
                    ret = [(i, j)]
                elif board[i][j] == max_power:
                    ret.append((i, j))
    nxt_ret = []
    min_attack = 1e9
    if len(ret) > 1:  # 가장 강한 파워를 가진 포탑이 여러 개인 경우
        for i, j in ret:
            if attack[i][j] < min_attack:
                min_attack = attack[i][j]
                nxt_ret = [(i, j)]
            elif attack[i][j] == min_attack:
                nxt_ret.append((i, j))
    else:
        return ret[0]

    ret = []
    min_row_col = 1e9
    if len(nxt_ret) > 1:  # 가장 약한 파워를 가진 포탑 중 최근 공격한 포탑이 여러 개인 경우
        for i, j in nxt_ret:
            if i + j < min_row_col:
                min_row_col = i + j
                ret = [(i, j)]
            elif i + j == min_row_col:
                ret.append((i, j))
    else:
        return nxt_ret[0]

    nxt_ret = []
    max_row = 0
    if len(ret) > 1:
        for i, j in ret:
            if i > max_row:
                max_row = i
                nxt_ret = i, j
        return nxt_ret
    else:
        return ret[0]


def work(x, y, sx, sy):
    # 레이저 공격이 가능하면 레이저 공격
    ret = dfs(x, y, sx, sy)
    power = board[x][y]
    p = power // 2

    attaked[x][y] = True
    attaked[sx][sy] = True
    board[sx][sy] = max(0, board[sx][sy] - power)

    if ret:
        for nx, ny in ret[:-1]:
            board[nx][ny] = max(0, board[nx][ny] - p)
            attaked[nx][ny] = True

    else:
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1), (1, 1), (-1, -1)]:
            nx, ny = sx + dx, sy + dy
            if 0 > nx:
                nx = N - 1
            if nx >= N:
                nx = 0
            if 0 > ny:
                ny = M - 1
            if ny >= M:
                ny = 0
            if (nx ,ny) == (x, y): continue
            board[nx][ny] = max(0, board[nx][ny] - p)
            attaked[nx][ny] = True


def dfs(x, y, sx, sy):
    v = [[False] * M for _ in range(N)]
    que = deque([(x, y, [])])
    v[x][y] = True

    while que:
        x, y, route = que.popleft()
        if x == sx and y == sy: return route

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 > nx:
                nx = N-1
            if nx >= N:
                nx = 0
            if 0 > ny:
                ny = M-1
            if ny >= M:
                ny = 0
            if board[nx][ny] == 0 or v[nx][ny]: continue
            que.append((nx, ny, route + [(nx, ny)]))
            v[nx][ny] = True


def recover():
    for i in range(N):
        for j in range(M):
            if not attaked[i][j] and board[i][j]:
                board[i][j] += 1


N, M, K = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(N)]
attack = [[0] * M for _ in range(N)]

for i in range(K):
    # 1개의 포탑만 남았다면 종료
    if end():
        break

    # 가장 약한 포탑 찾기
    x, y = weak_tower()
    attack[x][y] = i+1

    # 가장 강한 포탑 찾기
    sx, sy = strong_tower()

    board[x][y] += N + M
    # 경로 공격 or 포탄 공격
    attaked = [[False] * M for _ in range(N)]
    work(x, y, sx, sy)

    # 포탑 정비
    recover()

    # for i in range(N):
    #     print(board[i])
    # print()

ans = 0
for i in range(N):
    for j in range(M):
        ans = max(ans, board[i][j])
print(ans)
