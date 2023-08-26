N, M, K = map(int, input().split())
board = [[*map(int, input().split())]for _ in range(N)]
people = []
for _ in range(M):
    a, b = map(int, input().split())
    board[a-1][b-1] = -2
    people.append((a-1, b-1))
a, b = map(int, input().split())
board[a-1][b-1] = -1
exit = (a-1, b-1)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def move():
    global ans
    ret = []
    for i, (x, y) in enumerate(people):
        d = get_direction(x, y)
        nx, ny = x + dx[d], y + dy[d]
        if not (0 <= nx < N and 0 <= ny < N) or board[nx][ny] > 0: continue
        if (nx, ny) == exit:
            ret.append(i)
            board[x][y] = 0
            ans += abs(nx - x) + abs(ny - y)
            continue
        ans += abs(nx - x) + abs(ny - y)
        if board[x][y] != -1:
            board[x][y] = 0
        board[nx][ny] = -2
        people[i] = (nx, ny)

    for i in ret[::-1]:
        people.pop(i)



def get_direction(x, y):
    ddx = abs(exit[0] - x)
    ddy = abs(exit[1] - y)

    if ddx == 0 or ddy == 0:
        if ddx > ddy:     # 상하 이동
            if exit[0] > x: # 아래로 이동
                return 1
            else:
                return 3
        else:
            if exit[1] > y: # 오른쪽 이동
                return 0
            else:
                return 2
    else:
        ret = []
        if exit[0] > x:
            ret.append(1)
        else:
            ret.append(3)
        if exit[1] > y:
            ret.append(0)
        else:
            ret.append(2)

    for i in ret:
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] in [0, -1, -2]:
            return i
    return ret[0]


def get_min_square():
    max_square = get_max_square()

    for square_size in range(1, max_square+1):
        ret = is_possible_square_size(square_size)
        if ret:
            rotate_squre(ret[0], ret[1], ret[2])
            return


def get_max_square():
    ret = N-1 - exit[0]
    ret = max(ret, N-1 - exit[1])
    ret = max(ret, exit[0])
    ret = max(ret, exit[1])
    return ret


def is_possible_square_size(square_size):
    for sx in range(max(0, exit[0] - square_size), exit[0] + 1):
        for sy in range(max(0, exit[1] - square_size), exit[1] + 1):
            if is_possible(sx, sy, square_size):
                return sx, sy, square_size
    return False


def is_possible(sx, sy, square_size):
    for i in range(sx, sx + square_size + 1):
        for j in range(sy, sy + square_size + 1):
            for x, y in people:
                if (x, y) == (i, j):
                    return True


def rotate_squre(sx, sy, size):
    # 회전
    tmp = [[0] * (size+1) for _ in range(size+1)]
    for i in range(sx, sx + size+1):
        for j in range(sy, sy + size+1):
            tmp[i-sx][j-sy] = board[i][j]

    global exit, people
    people = []
    for i in range(size+1):
        for j in range(size+1):
            board[sx+i][sy+j] = tmp[size-j][i]
            if board[sx+i][sy+j] == -1:
                exit = (sx+i, sy+j)
    for i in range(N):
        for j in range(N):
            if board[i][j] == -2:
                people.append((i, j))
    # 출구 위치 찾기

    # 내구도 감소
    for x in range(sx, sx + size+1):
        for y in range(sy, sy + size+1):
            if board[x][y] > 0:
                board[x][y] -= 1
ans = 0
for i in range(K):
    move()
    if not people:
        break
    get_min_square()
print(ans)
print(exit[0] + 1, exit[1] + 1)
