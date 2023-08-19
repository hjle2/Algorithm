# 처음 토끼들은 전부 1,1에 있다.
# 가장 우선순위가 높은 토끼를 뽑아 멀리 보내주는 것을 k번 반복
# 우선순위는 점프 횟수가 적은 토끼, 행+열 번호가 작은 토끼, 행 번호가 작은 토끼, 열 번호가 작은 토끼, 고유 번호가 작은 토끼
# 상하좌우 네 방향으로 이동했을 때 위치를 구한다
# 이때 이동하는 도중 격자를 벗어나면 방향을 반대로 바꿔 한 칸 이동
# 구해진 위치 중 행+열 큰 칸, 행 큰 칸, 열 큰 칸 순으로 우선순위가 가잦ㅇ 높은 칸으로 토끼 이동
# 이 칸이 r, c 라 했을 때 i번 토끼를 제외한 나머지 토끼들은 전부 r+c 점수를 얻는다.
# 우선순위가 가장 높은 토끼를 뽑아 멀리 보내주는 것을 반복
# k 번 턴이 진행된 직후 행+열 큰 토끼, 행 큰 토끼, 열 큰 토끼, 고유번호 큰 토끼 순 중 가장 높은 토끼에게 점수 S를 더해준다.
# !! 꼭 한번이라도 뽑혔던 적이 있는 토끼 중에서 가장 우선순위가 높은 토끼를 골라야 한다
import sys
import heapq
input = sys.stdin.readline

total_sum = 0


def init(pid_d):
    global n, pids, dis, rabbits, rabbit_idx, scores
    n = len(pid_d) // 2
    pids = [0] * n
    dis = [0] * n               # 토끼들의 이동 거리
    scores = [0] * n            # 토끼들 점수

    rabbits = []                # 점프 횟수, 행+열, 행, 열, 고유
    rabbit_idx = {}             # 토끼들의 고유번호 - 인덱스
    for i in range(0, n * 2, 2):
        pids[i // 2] = pid_d[i]
        dis[i // 2] = pid_d[i + 1]
        rabbit_idx[pid_d[i]] = i // 2
        heapq.heappush(rabbits, (0, 2, 1, 1, pid_d[i]))


def get_rabbit():
    jump_cnt, _, r, c, pid = heapq.heappop(rabbits)
    return jump_cnt, r, c, pid


def get_rabbit_pt():
    # 그 중에서 행+열 번호가 가장 작은 토끼 구하기
    new_tmp = []
    max_rowcol = -1
    for i in range(n):
        _, _, x, y, pid = rabbits[i]
        if not is_runned[rabbit_idx[pid]]: continue
        if x + y > max_rowcol:
            max_rowcol = x + y
            new_tmp = [i]
        elif x + y == max_rowcol:
            new_tmp.append(i)
    # # 그 중에서 행 번호가 가장 작은 토끼 구하기
    tmp = []
    max_col = -1
    for i in new_tmp:
        _, _, x, y, _ = rabbits[i]
        if x > max_col:
            max_col = x
            tmp = [i]
        elif x == max_col:
            tmp.append(i)
    # # 그 중에서 열 번호가 가장 작은 토끼 구하기
    new_tmp = []
    max_row = -1
    for i in tmp:
        _, _, x, y, _ = rabbits[i]
        if y > max_row:
            max_row = y
            new_tmp = [i]
        elif y == max_row:
            new_tmp.append(i)
    # # 그 중에서 고유번호가 가장 작은 토끼 구하기
    max_idx = -1
    max_pid = -1
    for i in new_tmp:
        _, _, _, _, pid = rabbits[i]
        if pid > max_pid:
            max_pid = pid
            max_idx = rabbit_idx[pid]
    # # 토끼의 인덱스 반환해주기
    return max_idx


def move_rabbit(x, y, pid):
    # 토끼의 이동 거리만큼 4방향으로 이동시킨 결과 중에서
    idx = rabbit_idx[pid]
    move_result = []
    nx, ny = get_up_rabbit(x, y, dis[idx])
    move_result.append((nx, ny))

    nx, ny = get_down_rabbit(x, y, dis[idx])
    move_result.append((nx, ny))

    nx, ny = get_left_rabbit(x, y, dis[idx])
    move_result.append((nx, ny))

    nx, ny = get_right_rabbit(x, y, dis[idx])
    move_result.append((nx, ny))

    # 행+열이 가장 큰 칸 구하기
    tmp = []
    max_rowcol = -1
    for x, y in move_result:
        if x + y > max_rowcol:
            max_rowcol = x + y
            tmp = [(x, y)]
        elif x + y == max_rowcol:
            tmp.append((x, y))
    # 그 중에서 행이 가장 큰 칸 구하기
    new_tmp = []
    max_col = -1
    for x, y in tmp:
        if x > max_col:
            max_col = x
            new_tmp = [(x, y)]
        elif x == max_col:
            new_tmp.append((x, y))

    # 그 중에서 열이 가장 큰 칸 구하기
    tmp = []
    max_row = -1
    for x, y in new_tmp:
        if y > max_row:
            max_row = y
            tmp = (x, y)
    return idx, tmp[0], tmp[1]


def add_score(idx, score):
    global total_sum
    total_sum += score
    scores[idx] -= score


def change_d(pid, L):
    idx = rabbit_idx[pid]
    dis[idx] *= L


# 토끼를 위로 이동시킵니다.
def get_up_rabbit(x, y, dis):
    dis %= 2 * (N - 1)

    if dis >= x - 1:
        dis -= (x - 1)
        x = 1
    else:
        x -= dis
        dis = 0

    if dis >= N - x:
        dis -= (N - x)
        x = N
    else:
        x += dis
        dis = 0

    x -= dis

    return x, y


# 토끼를 아래로 이동시킵니다.
def get_down_rabbit(x, y, dis):
    dis %= 2 * (N - 1)

    if dis >= N - x:
        dis -= (N - x)
        x = N
    else:
        x += dis
        dis = 0

    if dis >= x - 1:
        dis -= (x - 1)
        x = 1
    else:
        x -= dis
        dis = 0

    x += dis

    return x, y


# 토끼를 왼쪽으로 이동시킵니다.
def get_left_rabbit(x, y, dis):
    dis %= 2 * (M - 1)

    if dis >= y - 1:
        dis -= (y - 1)
        y = 1
    else:
        y -= dis
        dis = 0

    if dis >= M - y:
        dis -= (M - y)
        y = M
    else:
        y += dis
        dis = 0

    y -= dis

    return x, y


# 토끼를 오른쪽으로 이동시킵니다.
def get_right_rabbit(x, y, dis):
    dis %= 2 * (M - 1)

    if dis >= M - y:
        dis -= (M - y)
        y = M
    else:
        y += dis
        dis = 0

    if dis >= y - 1:
        dis -= (y - 1)
        y = 1
    else:
        y -= dis
        dis = 0

    y += dis

    return x, y


def get_best_rabbit():
    ans = 0
    for i in range(n):
        ans = max(ans, total_sum + scores[i])
    print(ans)


for _ in range(int(input())):
    cmd = [*map(int, input().split())]
    if cmd[0] == 100:               # 경주 시작 준비
        N, M, P, *pid_d = cmd[1:]
        init(pid_d)

    elif cmd[0] == 200:             # 경주 진행
        K, S = cmd[1:]
        is_runned = [False] * n
        for _ in range(K):
            # 우선순위가 높은 토끼 구하기
            jump_cnt, r, c, pid = get_rabbit()
            # 우선순위가 높은 토끼를 이동시키기
            is_runned[rabbit_idx[pid]] = True
            idx, x, y = move_rabbit(r, c, pid)
            # 나머지 토끼들의 점수 올리기
            add_score(idx, x + y)
            heapq.heappush(rabbits, (jump_cnt + 1, x + y, x, y, pid))

        idx = get_rabbit_pt()
        scores[idx] += S

    elif cmd[0] == 300:             # 이동거리 변경
        pid_t, L = cmd[1:]
        # 고유번호가 pid_t인 토끼의 이동 거리를 L로 변경해준다
        change_d(pid_t, L)

    elif cmd[0] == 400:             # 최고의 토끼 선정
        get_best_rabbit()
