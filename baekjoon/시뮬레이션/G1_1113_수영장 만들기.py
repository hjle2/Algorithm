import sys
from collections import deque
input = sys.stdin.readline

res = 0

def in_range(r, c):
    return 0 <= r < n and 0 <= c < m

def bfs(r, c, h):
    global ret, visited

    que = deque([(r, c)])
    ispool = True
    visited[r][c] = True
    cnt = 1
    while que:
        r, c = que.popleft()

        for dr, dc in d:
            nr, nc = r + dr, c + dc

            if not in_range(nr, nc): # 외곽이라면 물이 새서 수영장이될 수 없다
                ispool = False
                continue

            if board[nr][nc] < h and not visited[nr][nc]:
                visited[nr][nc] = True
                que.append((nr, nc))
                cnt += 1

    if ispool:
        ret += cnt


d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m = map(int, input().split())
board = [[*map(int, [*input().rstrip()])] for _ in range(n)]
ret = 0

for h in range(1, 10): # 1~9의 수면 높이를 만들 수 있는 지 확인하기
    visited = [[False] * m for _ in range(n)]
    for r in range(n):
        for c in range(m): # 수면높이 h일 때 r, c좌표가 수영장이 될 수 있는 지 확인
            if board[r][c] < h and not visited[r][c]:
                bfs(r, c, h)
print(ret)
