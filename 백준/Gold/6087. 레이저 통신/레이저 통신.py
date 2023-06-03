from collections import deque

# 레이저를 찾는 함수
def find_c():
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'C':
                board[i][j] = '.'
                return i, j


def bfs(s, e):
    x, y = s
    que = deque([(x, y)])
    v = [[-1] * c for _ in range(r)]

    while que:
        x, y = que.popleft()

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy

            while 0 <= nx < r and 0 <= ny < c:
                if board[nx][ny] == '*':
                    break

                if v[nx][ny] != -1:
                    nx, ny = nx + dx, ny + dy
                    continue
                    
                if (nx, ny) == e:
                    return v[x][y] + 1

                que.append((nx, ny))
                v[nx][ny] = v[x][y] + 1
                nx, ny = nx + dx, ny + dy


c, r = map(int, input().split())
board = [[*input()] for _ in range(r)]

start = find_c()
end = find_c()

ans = bfs(start, end)
print(ans)