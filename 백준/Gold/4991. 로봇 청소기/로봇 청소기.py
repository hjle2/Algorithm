# 로봇의 위치 찾기
from collections import deque


def init():
    global pt, n
    pt = []
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'o':
                pt.insert(0, (i, j))
                board[i][j] = '.'
            elif board[i][j] == '*':
                pt.append((i, j))
    n = len(pt)
    make_graph()


def make_graph():
    global graph
    graph = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j: continue
            graph[i][j] = get_distance(i, j)


def get_distance(i, j):
    x, y = pt[i]
    que = deque()
    que.append((x, y, 0))
    v = [[False] * c for _ in range(r)]
    v[x][y] = True
    while que:
        x, y, dist = que.popleft()
        if (x, y) == pt[j]:
            return dist
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and not v[nx][ny] and board[nx][ny] != 'x':
                v[nx][ny] = True
                que.append((nx, ny, dist + 1))
    return 0

def solve():
    # 하나도 연결되어 있지 않은 노드가 있다면 모든 노드를 방문할 수 없음~
    for i in range(n):
        if sum(graph[i]) == 0:
            print(-1)
            return
    print(dfs(0, 1 << 0))


def dfs(cur, visited):
    # 모든 먼지를 청소했다면,
    if visited == (1 << n) - 1:
        return 0

    # 이미 계산되어 있는 최적값이 있다면 반환해주기
    if dp[cur][visited] != 0:
        return dp[cur][visited]

    dp[cur][visited] = 1e9
    for i in range(n):
        # 이미 청소한 먼지거나, 길이 없으면, 패스
        if visited & (1 << i) or graph[cur][i] == 0: continue
        dp[cur][visited] = min(dp[cur][visited], dfs(i, visited | (1 << i)) + graph[cur][i])
    return dp[cur][visited]

while True:
    c, r = map(int, input().split())
    if r == 0 and c == 0: break
    board = [[*input().rstrip()]for _ in range(r)]
    init()
    # i번째 먼지의 위치에 있을 때, 주은 먼지의 번호들의 집합 j
    dp = [[0] * (1 << n) for _ in range(n)]
    solve()