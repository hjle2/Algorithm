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
input = sys.stdin.readline

def init(pid_d):
    global jump_cnt, rabbit_pt, scores, n, pids, dis, rabbit_idx
    n = len(pid_d) // 2
    jump_cnt = [0] * n          # 토끼들의 점프 횟수
    scores = [0] * n            # 토끼들의 점수
    rabbit_pt = [[0, 0] for _ in range(n)]    # 토끼들의 위치
    pids = [0] * n               # 토끼들의 고유 번호
    dis = [0] * n                # 토끼들의 이동 거리

    rabbit_idx = {}             # 토끼들의 고유번호 - 인덱스
    for i in range(0, n * 2, 2):
        pids[i // 2] = pid_d[i]
        dis[i // 2] = pid_d[i + 1]
        rabbit_idx[pids[i // 2]] = i // 2


def get_rabbit():
    # 점프 횟수가 가장 적은 토끼 구하기
    tmp = []
    min_jump_cnt = 1e9
    for i in range(n):
        if jump_cnt[i] < min_jump_cnt:
            min_jump_cnt = jump_cnt[i]
            tmp = [i]
        elif jump_cnt[i] == min_jump_cnt:
            tmp.append(i)

    # 그 중에서 행+열 번호가 가장 작은 토끼 구하기
    new_tmp = []
    min_rowcol = 1e9
    for i in tmp:
        x, y = rabbit_pt[i]
        if x + y < min_rowcol:
            min_rowcol = x + y
            new_tmp = [i]
        elif x + y == min_rowcol:
            new_tmp.append(i)
    # 그 중에서 행 번호가 가장 작은 토끼 구하기
    tmp = []
    min_col = 1e9
    for i in new_tmp:
        x, y = rabbit_pt[i]
        if x < min_col:
            min_col = x
            tmp = [i]
        elif x == min_col:
            tmp.append(i)
    # 그 중에서 열 번호가 가장 작은 토끼 구하기
    new_tmp = []
    min_row = 1e9
    for i in tmp:
        x, y = rabbit_pt[i]
        if y < min_row:
            min_row = y
            new_tmp = [i]
        elif y == min_row:
            new_tmp.append(i)
    # 그 중에서 고유번호가 가장 작은 토끼 구하기
    min_idx = 0
    min_pid = 1e9
    for i in new_tmp:
        pid = pids[i]
        if pid < min_pid:
            min_pid = pid
            min_idx = i
    # 토끼의 인덱스 반환해주기
    return min_idx


def get_rabbit_pt():
    # 그 중에서 행+열 번호가 가장 작은 토끼 구하기
    new_tmp = []
    max_rowcol = 0
    for i in range(n):
        x, y = rabbit_pt[i]
        if x + y > max_rowcol:
            max_rowcol = x + y
            new_tmp = [i]
        elif x + y == max_rowcol:
            new_tmp.append(i)
    # 그 중에서 행 번호가 가장 작은 토끼 구하기
    tmp = []
    max_col = 0
    for i in new_tmp:
        _, y = rabbit_pt[i]
        if y > max_col:
            max_col = y
            tmp = [i]
        elif y == max_col:
            tmp.append(i)
    # 그 중에서 열 번호가 가장 작은 토끼 구하기
    new_tmp = []
    max_row = 0
    for i in new_tmp:
        x, _ = rabbit_pt[i]
        if x < max_row:
            max_row = x
            tmp = [i]
        elif x == max_row:
            tmp.append(i)
    # 그 중에서 고유번호가 가장 작은 토끼 구하기
    max_idx = 0
    max_pid = 0
    for i in new_tmp:
        pid = pids[i]
        if pid > max_pid:
            max_pid = pid
            max_idx = i
    # 토끼의 인덱스 반환해주기
    return max_idx


def move_rabbit(idx):
    # 토끼의 이동 거리만큼 4방향으로 이동시킨 결과 중에서
    x, y = rabbit_pt[idx]
    ox, oy = x, y
    move_result = []
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        dd = dis[idx]
        nx, ny = x, y
        while dd:
            nx, ny = nx + dx, ny + dy
            dd -= 1
            if not (0 <= nx < N and 0 <= ny < M):
                dx *= -1
                dy *= -1
                nx, ny = nx + dx * 2, ny + dy * 2
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
    rabbit_pt[idx] = (tmp[0], tmp[1])
    # 이동시킨 결과 좌표 합 반환
    return idx, tmp[0] + 1 + tmp[1] + 1


def add_score(idx, score):
    for i in range(n):
        if i == idx: continue
        scores[i] += score


def change_d(pid, L):
    idx = rabbit_idx[pid]
    dis[idx] *= L


for _ in range(int(input())):
    cmd = [*map(int, input().split())]
    if cmd[0] == 100:               # 경주 시작 준비
        N, M, P, *pid_d = cmd[1:]
        init(pid_d)

    elif cmd[0] == 200:             # 경주 진행
        K, S = cmd[1:]

        for _ in range(K):
            # 우선순위가 높은 토끼 구하기
            idx = get_rabbit()
            # 우선순위가 높은 토끼를 이동시키기
            idx, score = move_rabbit(idx)
            # 나머지 토끼들의 점수 올리기
            add_score(idx, score)
            jump_cnt[idx] += 1

        idx = get_rabbit_pt()
        scores[idx] += S

    elif cmd[0] == 300:             # 이동거리 변경
        pid_t, L = cmd[1:]
        # 고유번호가 pid_t인 토끼의 이동 거리를 L로 변경해준다
        change_d(pid_t, L)

    elif cmd[0] == 400:             # 최고의 토끼 선정
        print(max(scores))
