from collections import deque


def find_prisoner():
    prisoner = [(0, 0)]
    for i in range(1, r-1):
        for j in range(1, c-1):
            if board[i][j] == '$':
                prisoner.append((i, j))
    return prisoner


def bfs(pt):
    x, y = pt
    v = [[-1] * c for _ in range(r)]
    v[x][y] = 0
    que = deque([(x, y)])
    while que:
        x, y = que.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 > nx or 0 > ny or nx >= r or ny >= c or v[nx][ny] != -1 or board[nx][ny] == '*': continue
            if board[nx][ny] == '#':
                v[nx][ny] = v[x][y] + 1
                que.append((nx, ny))
            else:
                v[nx][ny] = v[x][y]
                que.appendleft((nx, ny))
    return v


def in_range(x, y):
    return 0 <= x < r and 0 <= y < c


def get_ans(one, two, three):
    ans = 1e9
    for i in range(r):
        for j in range(c):
            if one[i][j] == -1 or two[i][j] == -1 or three[i][j] == -1:
                continue
            tmp = one[i][j] + two[i][j] + three[i][j]
            if board[i][j] == '#':
                tmp -= 2
            ans = min(ans, tmp)
    return ans


for _ in range(int(input())):
    r, c = map(int, input().split())
    board = [['.', *input().rstrip(), '.']for _ in range(r)]
    r += 2
    c += 2
    board.insert(0, ['.'] * c)
    board.append(['.'] * c)
    prisoners = find_prisoner()
    one = bfs(prisoners[0])
    two = bfs(prisoners[1])
    three = bfs(prisoners[2])

    print(get_ans(one, two, three))
