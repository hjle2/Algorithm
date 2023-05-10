from collections import deque

r, c = map(int, input().split())
board = [[*input().rstrip()]for _ in range(r)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


# 얼음 좌표 얻기
def get_water():
    water = deque([])
    for i in range(r):
        for j in range(c):
            if board[i][j] != 'X':
                water.append((i, j))
    return water


# 백조의 좌표
def get_a_swan():
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'L':
                return (i, j)


# 백조 둘이 만날 수 있는지
def can_meet():
    global swan
    new_swan = deque([])

    while swan:
        x, y = swan.popleft()

        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if not in_range(nx, ny) or visited[nx][ny]: continue

            if board[nx][ny] == '.':
                visited[nx][ny] = True
                swan.append((nx, ny))

            elif board[nx][ny] == 'X':
                new_swan.append((nx, ny))
                visited[nx][ny] = True

            else:
                return True
    swan = new_swan
    return False


def melt():
    global water
    new_water = deque([])
    while water:
        x, y = water.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if not in_range(nx, ny): continue
            if board[nx][ny] == 'X':
                new_water.append((nx, ny))
                board[nx][ny] = '.'
    water = new_water


def in_range(x, y):
    return 0 <= x < r and 0 <= y < c


visited = [[False] * c for _ in range(r)]
# 두 백조의 좌표
swan = get_a_swan()
visited[swan[0]][swan[1]] = True
swan = deque([swan])

# 얼음이 있는 좌표들
water = get_water()
day = 0
while not can_meet():
    melt()
    day += 1
print(day)