from collections import deque

def bfs(r, c):
    que = deque([(r, c, 1)])
    while que:
        r, c, t = que.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            while 0<=nr<H and 0<=nc<W and A[nr][nc] != '*':
                if not visited[nr][nc] and A[nr][nc] == 'C':
                    return t
                if not visited[nr][nc]:
                    visited[nr][nc] = t+1
                    que.append((nr, nc, t+1))
                nr += dr
                nc += dc


d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
W, H = map(int, input().split())
A = []
laser = []
for i in range(H):
    ar = [*input()]
    if 'C' in ar:
        laser.append((i, ar.index('C')))
    A.append(ar)

visited = [[0]*W for _ in range(H)]
r, c = laser.pop(0)
visited[r][c] = 1
print(bfs(r, c) - 1)
