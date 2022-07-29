# 유저가 경로를 설정하는 로봇 청소기
# 모두 깨끗한 칸으로 만드는 데 필요한 이동 횟수의 최솟 값
# 로봇의 위치 + 먼지들의 위치 각 거리 중 최솟 값이 되는 경우를 구하면 되는 거 아닌가 ㅎ
def getDistance(pt1, pt2):
    ox, oy = pt1
    ex, ey = pt2
    que = [(ox, oy, 0)]
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False]*w for _ in range(h)]
    visited[pt1[0]][pt1[1]] = True
    while que:
        ox, oy, d = que.pop(0)
        if ox == ex and oy == ey:
            return d
        for i, j in d:
            x, y = ox + i, oy + j
            if 0<=x<h and 0<=y<w and not visited[x][y]:
                visited[x][y] = True
                que.append((x, y, d + 1))


def solve(pt):
    dist = [[0]*len(pt) for _ in range(len(pt))]
    for i in range(len(pt)):
        for j in range(i+1, len(pt)):
            d = getDistance(pt[i], pt[j])
            dist[i][j] = d
            dist[j][i] = d


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    ar = []
    pt = []
    cnt = 0
    robot = (0, 0)
    for i in range(h):
        tmp = [*input()]
        for j in range(w):
            if tmp[j] == '*':
                cnt += 1
                pt.append((i, j))
            elif tmp[j] == 'o':
                # robot = (i, j)
                pt.append((i, j))
        ar.append(tmp)



