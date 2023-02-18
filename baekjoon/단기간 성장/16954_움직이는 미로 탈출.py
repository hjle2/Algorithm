# 체판은 빈칸 또는 벽
# 왼쪾 아래칸에 위치한 캐릭터가 오, 위로 이동해야 한다
# 벽이 1초마다 한칸씩 내려가고, 맨 아래에 있다면, 사라진다
# 인접한 한칸 또는, 대각선으로 이동하거나 이동하지 않음
# 빈칸으로만 이동 가능
# 캐릭터 먼저 이동, 벽이 이동
# 벽이 캐릭터가 있는 칸으로 내려가면 종료..
def bfs():
    que = [(N-1, 0)]
    visited[N-1][0] = 0
    while que:
        x, y = que.pop()
        for nx, ny in move(x, y):
            if nx == 0:
                return 1
            if not visited[nx][ny]:
                que.append((nx-1, ny))
                visited[nx][ny] = 1
    return 0


def fallWall():
    ar.pop()
    ar.insert(0, (['.']*N))


def move(x, y):
    d = [(-1, 1), (-1, 0), (0, 1), (0, 0), (1, 1), (-1, -1), (0, -1), (1, 0), (1, -1)]
    ans = []
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if nx == 0 and ny == N-1:
            ans.append((nx, ny))
        if 0<=nx<N and 0<=ny<N and ar[nx][ny] == '.':
            if 0<=nx-1 and ar[nx-1][ny] == '.' or nx-1 < 0:
                ans.append((nx, ny))
    return ans

N = 8
ar = [[*input()]for _ in range(N)]
x, y = N-1, 0
visited = [[0]*N for _ in range(N)]
print(bfs())
# ######..
# .#.#.###
# ........
# ........
# ........
# ........
# ........
# ........