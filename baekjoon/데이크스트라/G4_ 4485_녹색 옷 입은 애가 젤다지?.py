# 게임의 화폐 단위 루피
# 도둑 루피를 획득하면 루피가 감소한다
# 주인공은 0,0에 있다
# 잃을 수 밖에 없는 최소 금액은?
import heapq
import sys

input = sys.stdin.readline

def solve():
    q = [(A[0][0], (0, 0))]
    visited = [[1e9]*N for _ in range(N)]
    visited[0][0] = A[0][0]
    while q:
        r, pt = heapq.heappop(q)
        x, y = pt
        if visited[x][y] < r: continue
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] > A[nx][ny] + r:
                visited[nx][ny] = A[nx][ny] + r
                heapq.heappush(q, (visited[nx][ny], (nx, ny)))
    return visited[N-1][N-1]


t = 1
while 1:
    N = int(input())
    if N == 0: break
    A = [[*map(int, input().split())]for _ in range(N)]
    print('Problem ', t, ": ", solve(), sep='')
    t += 1