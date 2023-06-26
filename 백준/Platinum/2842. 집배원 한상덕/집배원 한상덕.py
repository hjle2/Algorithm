from collections import deque


def bfs(l, r):
    x, y = graph[0]
    cnt = 0
    que = deque([(x, y)])
    v = [[False] * n for _ in range(n)]
    v[x][y] = True
    while que:
        x, y = que.popleft()
        if board[x][y] in ['P', 'K']:
            cnt += 1

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < n) or v[nx][ny]: continue
            if l <= height[nx][ny] <= r:
                que.append((nx, ny))
                v[nx][ny] = True

    return True if cnt == len(graph) else False


n = int(input())
board = [[*input()]for _ in range(n)]
height = [[*map(int, input().split())]for _ in range(n)]

ar_height = set()
graph = []
for i in range(n):
    for j in range(n):
        ar_height.add(height[i][j])
        if board[i][j] in ['P', 'K']:
            graph.append((i, j))
ar_height = sorted(ar_height)

l, r = 0, 0
ans = 1e9
x, y = graph[0]
while l < len(ar_height):
    k = 0
    if ar_height[l] <= height[x][y] <= ar_height[r]:
        k = bfs(ar_height[l], ar_height[r])
    if k:
        ans = min(ans, ar_height[r] - ar_height[l])
        if ans == 0:
            break
        l += 1
    elif r + 1 < len(ar_height):
        r += 1
    else:
        break
print(ans)