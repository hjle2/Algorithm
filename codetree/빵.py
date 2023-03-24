from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# n: 격자 크기, m: 사람 수
n, m = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(n)]
cv_store = []
for i in range(m):
    a, b = map(int, input().split())
    cv_store.append((a-1, b-1))

# 사람의 위치
people_pt = [[] for _ in range(m)]
# 도착 여부
people_done = [False] * m


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def get_closest_basecamp(i):
    x, y = cv_store[i]
    v = [[False] * n for _ in range(n)]
    v[x][y] = True

    que = deque([(x, y)])
    while que:
        x, y = que.popleft()
        if board[x][y] == 1:
            return x, y
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if not in_range(nx, ny) or v[nx][ny] or board[nx][ny] == -1: continue
            v[nx][ny] = True
            que.append((nx, ny))


def get_closest_direction(x, y, i):
    cx, cy = cv_store[i]  # 편의점 좌표
    v = [[False] * n for _ in range(n)]
    que = deque([])

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if not in_range(nx, ny) or board[nx][ny] == -1: continue
        v[nx][ny] = True
        que.append((nx, ny, d))

    while que:
        x, y, d = que.popleft()
        if (x, y) == (cx, cy):  # 편의점에 도착했을 때
            return d
        for di in range(4):
            nx, ny = x + dx[di], y + dy[di]
            if not in_range(nx, ny) or v[nx][ny] or board[nx][ny] == -1: continue
            v[nx][ny] = True
            que.append((nx, ny, d))


def move(time):
    for people_idx in range(m):
        if time < people_idx: break
        # 베이스캠프로 이동
        if time < m and not people_pt[people_idx]:
            x, y = get_closest_basecamp(time)
            people_pt[time] = (x, y)
            board[x][y] = -1  # 다른 사람이 방문할 수 없음 처리
        else:
            if people_done[people_idx]: continue
            x, y = people_pt[people_idx]
            # 이동하기
            d = get_closest_direction(x, y, people_idx)
            nx, ny = x + dx[d], y + dy[d]
            if (nx, ny) == cv_store[people_idx]:
                people_done[people_idx] = True
                board[nx][ny] = -1  # 다른 사람이 방문할 수 없음 처리
            else:
                people_pt[people_idx] = (nx, ny)


time = 0
# 모두 도착할 때까지 반복!!
while not all(people_done):
    move(time)
    time += 1

print(time)
