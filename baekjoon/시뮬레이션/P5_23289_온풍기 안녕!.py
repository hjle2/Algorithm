def start():
    choco_cnt = 0
    while choco_cnt < 101:

        work_all()          # 온풍기 작동

        adjust()        # 온도 조절

        get_cold_edge() # 가장 바깥 온도 1 감소

        choco_cnt+=1    # 초콜릿 먹기


        if check_tmp():   # 온도 확인
            break

    print(choco_cnt)


def work_all():
    for r, c, d in onpung:
        work(r, c, d)


def work(r, c, d):
    r, c = r + dr[d], c + dc[d]
    q = [(r, c, 5)] # 첫번째 칸은 온풍기 파워 5
    v = [[False] * C for _ in range(R)]
    v[r][c] = True

    while q:
        r, c, p = q.pop(0)
        A[r][c] += p

        if p == 1: continue

        for drt in direction[d]:
            nr, nc = r + dr[drt], c + dc[drt]

            if nr < 0 or nc < 0 or nr >= R or nc >= C or v[nr][nc]: continue
            if isWall(r, c, drt, d): continue

            q.append((nr, nc, p-1))
            v[nr][nc] = True

            

def isWall(r, c, d, onpung_d = 0):
    if d == 0:      # 오른쪽 이동
        return cwall[r][c+1]
    elif d == 1:    # 왼쪽 이동
        return cwall[r][c]
    elif d == 2:    # 위쪽 이동
        return rwall[r][c]
    elif d == 3:    # 아래쪽 이동
        return rwall[r+1][c]
    elif d == 4:    # 위 오른쪽 이동
        if onpung_d == 0:   # 온풍기의 방향이 오른쪽
            return isWall(r, c, 2) or isWall(r-1, c, 0)
        else:               # 온풍기의 방향이 위쪽
            return isWall(r, c, 0) or isWall(r, c+1, 2)
    elif d == 5:    # 위 왼쪽 이동
        if onpung_d == 1:   # 온풍기의 방향이 왼쪽
            return isWall(r, c, 2) or isWall(r-1, c, 1)
        else:               # 온풍기의 방향이 위쪽
            return isWall(r, c, 1) or isWall(r, c-1, 2)
    elif d == 6:    # 아래 오른쪽 이동
        if onpung_d == 0:   # 온풍기의 방향이 오른쪽
            return isWall(r, c, 3) or isWall(r+1, c, 0)
        else:               # 온풍기의 방향이 아래쪽
            return isWall(r, c, 0) or isWall(r, c+1, 3)
    elif d == 7:    # 아래 왼쪽 이동
        if onpung_d == 1:   # 온풍기의 방향이 왼쪽
            return isWall(r, c, 3) or isWall(r+1, c, 1)
        else:               # 온풍기의 방향이 아래쪽
            return isWall(r, c, 1) or isWall(r, c-1, 3)


def adjust():
    tmp = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if A[r][c] < 4: continue

            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if isWall(r, c, d): continue
                if 0 <= nr < R and 0 <= nc < C and A[nr][nc] + 4 <= A[r][c]:
                    t = (A[r][c] - A[nr][nc])//4
                    tmp[r][c] -= t
                    tmp[nr][nc] += t

    for r in range(R):
        for c in range(C):
            if not tmp[r][c]: continue
            A[r][c] += tmp[r][c]


def get_cold_edge():
    for r in range(R):
        if r == 0 or r == R-1:
            crange = range(C)
        else:
            crange = [0, C-1]
        for c in crange:
            if A[r][c] > 0:
                A[r][c] -= 1


def check_tmp():
    for r, c in check:
        if A[r][c] < K: return False
    return True


R, C, K = map(int, input().split())
onpung = []     # 온풍기의 행, 열, 작동 방향
check = []      # 온도를 조사할 좌표들
rwall = [[False] * (C+1)for _ in range(R+1)]    # 가로 벽
cwall = [[False] * (C+1)for _ in range(R+1)]    # 세로 벽

# 온풍기의 방향과 같이 우, 좌, 상, 하 + 온풍기의 작동 방향 때문에 우상, 좌상, 우하, 좌하
dr = [0, 0, -1, 1, -1, -1, 1, 1]
dc = [1, -1, 0, 0, 1, -1, 1, -1]

# 온풍기의 진행 방향
direction = [(0, 4, 6), (1, 5, 7), (2, 4, 5), (3, 6, 7)]

A = [[0] * C for _ in range(R)]

for r in range(R):
    a = [*map(int, input().split())]
    for c in range(C):
        if not a[c]: continue

        if a[c] == 5:
            check.append((r, c))
        else:
            onpung.append((r, c, a[c] - 1))


W = int(input())
for _ in range(W):
    x, y, t = map(int, input().split())
    if t:   # t가 1이면 세로 벽
        cwall[x-1][y] = True
    else:
        rwall[x-1][y-1] = True
            

start()