from collections import deque


def throw(n, x):
    rg = [range(c), range(c-1, -1, -1)][n%2]
    for y in rg:
        if board[x][y] == 'x':
            board[x][y] = '.'
            return (x, y)


def in_range(x, y):
    return 0 <= x < r and 0 <= y < c


def fall():
    clusters = []
    for i in range(r):
        for j in range(c):
            if board[i][j] == '.' or v[i][j]: continue
            cluster = get_clusters(i, j)
            clusters.append(cluster)
    if len(clusters) == 1:
        return

    for cluster in clusters:
        cluster.sort(key=lambda x:-x[0])
        if not is_intheair(cluster): continue

        fall_height = get_fall_height(cluster)
        for x, y in cluster:
            board[x+fall_height][y] = 'x'
            board[x][y] = '.'


def get_fall_height(cluster):
    ret = r
    for x, y in cluster:
        flag = True
        for i in range(x+1, r):
            if board[i][y] == 'x':
                if (i, y) in cluster: continue
                flag = False
                ret = min(ret, i-x-1)
                break
        if flag:
            ret = min(ret, r - x - 1)
    return ret


def is_intheair(cluster):
    for x, y in cluster:
        if x == r-1: # 하나라도 바닥에 닿아 있으면 공중에 떠있지 않음
            return False
    return True


def get_clusters(x, y):
    ret = []
    que = deque([(x, y)])
    v[x][y] = True
    while que:
        x, y = que.popleft()
        ret.append((x, y))
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if not in_range(nx, ny) or v[nx][ny] or board[nx][ny] == '.': continue
            que.append((nx, ny))
            v[nx][ny] = True
    return ret


r, c = map(int, input().split())
board = [[*input().rstrip()]for _ in range(r)]
n = int(input())
height = [*map(int, input().split())]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i in range(n):
    # 맞은 미네랄의 위치
    pt = throw(i, r-height[i])
    # 맞은 미네랄이 없다면 패스
    if not pt: continue
    x, y = pt

    # 클러스터가 쪼개지지 않았다면 패스
    v = [[False] * c for _ in range(r)]
    fall()

for i in range(r):
    print(''.join(board[i]))