from collections import deque

def bfs(r, c):
    q = deque([(r, c)])
    dist  = [[-1]*C for _ in range(R)]
    dist[r][c] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0<=nr<R and 0<=nc<C and dist[nr][nc] < 0 and A[nr][nc] != '*':
                if A[nr][nc] == '.':
                    dist[nr][nc] = dist[r][c]
                    q.appendleft((nr, nc))
                elif A[nr][nc] == '#':
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
    return dist


def find_prisoner():
    que = deque([(0, 0)])
    for r in range(R):
        for c in range(C):
            if A[r][c] == '$':
                que.append((r, c))
                A[r][c] = '.'
    return que


d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for _ in range(int(input())):
    R, C = map(int, input().split())
    A = [['.', *input().rstrip(), '.']for _ in range(R)]
    R, C = R+2, C+2
    A.insert(0, ['.'] * C)
    A.append(['.'] * C)

    que = find_prisoner()
    r, c = que.popleft()
    d1 = bfs(r, c)
    r, c = que.popleft()
    d2 = bfs(r, c)
    r, c = que.popleft()
    d3 = bfs(r, c)

    ans = R * C
    for r in range(R):
        for c in range(C):
            if d1[r][c] >= 0 and d2[r][c] >= 0 and d3[r][c] >= 0:
                k = d1[r][c] + d2[r][c] + d3[r][c]
                if A[r][c] == '#': k -= 2
                ans = min(ans, k)
    print(ans)

