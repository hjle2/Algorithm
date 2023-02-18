# 검은 방은 들어갈 수 없다
# 서로 붙어있는 흰 방은 지나 다닐 수 있다
# 윗 줄 맨 왼쪽 방과 맨 오른쪽 아래 는 시작과 끝 방으로 흰 방이다
# 시작에서 출발해서 길을 찾아 끝 방으로 가는는 중 되도록 적은 수의 검은 색 방을 바꾸는 경우의 개수 출력
import sys;import heapq
input = sys.stdin.readline

def dijkstra():
    d = [[1e9]*N for _ in range(N)]
    d[0][0] = 0
    q = [(0, (0, 0))]
    while q:
        w, pt = heapq.heappop(q)
        x, y = pt
        if d[x][y] < w: continue
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0<=nx<N and 0<=ny<N and d[nx][ny] > w + (not A[nx][ny]):
                d[nx][ny] = w + (not A[nx][ny])
                heapq.heappush(q, (d[nx][ny], (nx, ny)))
    print(d[N-1][N-1])


N = int(input())
A = [[*map(int, [*input()][:-1])]for _ in range(N)]
dijkstra()