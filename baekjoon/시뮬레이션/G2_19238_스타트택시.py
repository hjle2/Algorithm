# 손님을 도착지로 데려다주면 -> 연료 충전
# 연료 0 -> 업무 종료
# 목표는 M 명의 승객을 태우는 것
# 한번에 한명의 승객만 태울 수 있음
from collections import deque


# 태울 승객을 고를 때 현재 위치에서 최단거리가 가장 짧은 승객
# 그 중 행 번호가 가장 작은 승객
# 그 중 열 번호가 가장 작은 승객 순으로 태운다

# 연료는 1칸 이동당 1씩 소모
# 소모한 연료양의 두배가 충전된다
# 이동 중 연료가 바닥나면 이동 실패 그리고 업무 종료
# 도착과 동시에 연료가 바닥나는 것은 성공한 것으로 간주한다

def get_closest(r, c):
    q = deque()
    q.append((r, c, 0))
    v = [[False] * N for _ in range(N)]
    v[r][c] = True
    min_cnt = INF
    ret = []
    while q:
        r, c, cnt = q.popleft()
        if A[r][c] < 0: # 승객이 있는 위치
            if min_cnt == cnt:
                ret.append((r, c))
            elif min_cnt > cnt:
                min_cnt = cnt
                ret = [(r, c)]
            continue
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            # 격자 범위 내, 방문하지 않은 곳, 벽이 아닌 곳
            if 0 <= nr < N and 0 <= nc < N and not v[nr][nc] and A[nr][nc] != 1:
                v[nr][nc] = True
                q.append((nr, nc, cnt+1))

    ret.sort()
    if ret:
        return ret[0][0],ret[0][1], min_cnt
    return


def get_distance(sr, sc, er, ec):
    q = deque()
    q.append((sr, sc, 0))
    v = [[False] * N for _ in range(N)]
    v[sr][sc] = True
    while q:
        r, c, cnt = q.popleft()
        if r == er and c == ec:
            return cnt
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            # 격자 범위 내, 방문하지 않은 곳, 벽이 아닌 곳
            if 0 <= nr < N and 0 <= nc < N and not v[nr][nc] and A[nr][nc] != 1:
                v[nr][nc] = True
                q.append((nr, nc, cnt+1))
    return


INF = 1e9
N, M, F = map(int, input().split())
A = [[*map(int, input().split())]for _ in range(N)]
r, c = map(lambda x:int(x) -1, input().split())
dest = [0]
for i in range(M):
    sr, sc, er, ec = map(int, input().split())
    A[sr-1][sc-1] = -i-1            # 승객 정보는 지도에 음수로 표시
    dest.append((er-1, ec-1))      # 승객의 도착지 정보는 승객의 음수값을 절댓값취한 인댁스에 담아둔다


cnt = 0
while cnt < M:
    rcd = get_closest(r, c)
    if not rcd:
        break
    er, ec, dist = rcd

    if F < dist:        # 승객을 태우러 갈 수 없으면 운행 종료
        break

    r, c = er, ec       # 승객을 태움
    F -= dist

    er, ec = dest[-A[r][c]]  # 도착지 정보
    A[r][c] = 0

    dist = get_distance(r, c, er, ec)
    if not dist or F < dist:
        break
    r, c = er, ec
    F += dist

    cnt += 1


print(F if cnt == M else -1)
