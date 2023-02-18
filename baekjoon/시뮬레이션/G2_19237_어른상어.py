def only_one():
    for r in range(N):
        for c in range(N):
            if A[r][c] > 1:
                return False
    return True


def leave_smell():
    for r in range(N):
        for c in range(N):
            if A[r][c]:
                smell[r][c] = K
                smell_n[r][c] = A[r][c]


def move():
    tmp = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if A[r][c]:
                nr, nc, nd = get_next(r, c)
                shark_dic[A[r][c]-1] = nd   # 방향 전환

                if tmp[nr][nc]:             # 이미 상어가 있으면 더 작은 상어만 존재
                    if tmp[nr][nc] > A[r][c]:
                        tmp[nr][nc] = A[r][c]
                else:
                    tmp[nr][nc] = A[r][c]   # 상어가 없으면 그냥 이동
    return tmp


def get_next(r, c):
    my_smell = []
    d = shark_dic[A[r][c]-1]
    for d in shark_prio[A[r][c] - 1][d]:
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            if not smell[nr][nc]:           # 인접 방향 중 냄새가 없는 곳으로 이동
                return nr, nc, d
            if not my_smell and smell_n[nr][nc] == A[r][c]:
                my_smell = (nr, nc, d)
    return my_smell                         # 인접 방향 중 냄새가 없는 곳이 없으면 자기 냄새가 있는 곳으로 이동


def remove_smell():
    for r in range(N):
        for c in range(N):
            if smell[r][c]:
                smell[r][c] -= 1
                if smell[r][c] == 0:
                    smell_n[r][c] = 0


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M, K = map(int, input().split())
A = [[*map(int, input().split())]for _ in range(N)]

shark_dic = [*map(lambda x:int(x)-1, input().split())]
shark_prio = [[[*map(lambda x: int(x) - 1, input().split())] for _ in range(4)] for _ in range(M)]
smell = [[0] * N for _ in range(N)]
smell_n = [[0] * N for _ in range(N)]

time = 0
while time <= 1000 and not only_one():

    leave_smell()

    A = move()

    remove_smell()
    time += 1

print(time if time <= 1000 else -1)
