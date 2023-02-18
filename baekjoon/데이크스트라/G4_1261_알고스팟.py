# 미로의 벽을 부수면 이동 가능
# 운영진 여러명은 모두 같은 방에 있어야 한다
# 이동 가능한 방은 상하 좌우 인접한 빈 방
import heapq

M, N = map(int, input().split())
A = [[*map(int, [*input()])]for _ in range(N)]
D = [[-1] * M for _ in range(N)]
q = [(0, (0, 0))]
visited = [[0]*M for _ in range(N)]
visited[0][0] = 1

while q:
    c, pt = heapq.heappop(q)
    x, y = pt
    if x == N-1 and y == M-1 :
        print(c)
        break
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            visited[nx][ny] = 1
            if A[nx][ny] == 1:
                heapq.heappush(q, (c+1, (nx, ny)))
            else:
                heapq.heappush(q, (c, (nx, ny)))
