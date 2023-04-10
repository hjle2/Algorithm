from collections import deque
def solve():
    board = [[-1] * n for _ in range(n)]
    board[hx][hy] = 0
    que = deque([(hx, hy, 0)])
    while que:
        x, y, d = que.popleft()

        if x == ex and y == ey:
            return d

        for dx, dy in [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and board[nx][ny] < 0:
                que.append((nx, ny, d + 1))
                board[nx][ny] = d + 1


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


for _ in range(int(input())):
    n = int(input())
    hx, hy = map(int, input().split())
    ex, ey = map(int, input().split())
    print(solve())
