# 위치 가능성이 있는 갯수
# 시간당 1
from collections import deque

dr = [[0, 0, 1, -1], [1, -1], [0, 0], [-1, 0], [0, 1], [0, 1], [-1, 0]]
dc = [[1, -1, 0, 0], [0, 0], [1, -1], [0, 1], [1, 0], [-1, 0], [0, -1]]

def isconnected(r,c, nr,nc):
    for x, y in [(r, c), (nr, nc)]:
        tag = False
        v = a[x][y] - 1
        ir = [4, 2][v>0]
        for i in range(ir):
            nx, ny = x + dr[v][i], y + dc[v][i]
            if nx == nr and ny == nc:
                tag = True
            elif nx == r and ny == c:
                tag = True
        if not tag: return False
    return True

def bfs(r, c):
    cnt = 0
    que = deque([(r, c, 1)])
    vis[r][c] = True
    while que:
        r, c, d = que.popleft()
        if d > h: break
        cnt += 1
        v = a[r][c]-1
        i_r = 4 if v == 0 else 2
        for i in range(i_r):
            nr, nc = r + dr[v][i], c + dc[v][i]
            if 0<=nr<n and 0<=nc<m and not vis[nr][nc] and a[nr][nc]:
                if isconnected(r, c, nr, nc):
                    vis[nr][nc] = True
                    que.append((nr, nc, d+1))
    return cnt


for t in range(int(input())):
    n, m, r, c, h = map(int, input().split())
    a = [list(map(int, input().split()))for _ in range(n)]
    vis = [[False]*m for _ in range(n)]
    print(f'#{t+1}', bfs(r, c))