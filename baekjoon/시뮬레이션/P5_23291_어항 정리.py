N, K = map(int, input().split())
tank = [[0] * N for _ in range(N)]
tank[-1] = [*map(int, input().split())]
MIN_FISH = 999999


def get_max_min_diff():
    global MIN_FISH
    MIN_FISH = min(tank[-1])
    return max(tank[-1]) - MIN_FISH


def add_fish():
    for i in range(N):
        if tank[-1][i] == MIN_FISH:
            tank[-1][i] += 1


def stack():
    w, h, cur = 1, 1, 0
    while cur - 1 + w + h < N:
        for i in range(w):
            for j in range(h):
                r, c = N - h + j, cur + i
                nr, nc = N-1-w+i, cur - 1 + w + h - j
                tank[nr][nc], tank[r][c] = tank[r][c], 0

        cur += w
        if w == h:
            h += 1
        else:
            w += 1


def adjust():
    adj = [[0] * N for _ in range(N)]
    for c in range(N):
        for r in range(N-1, -1, -1):
            if not tank[r][c]: break
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and tank[nr][nc]:
                    diff = tank[nr][nc] - tank[r][c]
                    diff //= 5
                    if diff <= 0: continue
                    adj[nr][nc] -= diff
                    adj[r][c] += diff

    for c in range(N):
        for r in range(N-1, -1, -1):
            if not tank[r][c]: break
            tank[r][c] += adj[r][c]


def unstack():
    temp = []
    for c in range(N):
        for r in range(N-1, -1, -1):
            if not tank[r][c]: break
            temp.append(tank[r][c])
            tank[r][c] = 0
    tank[-1] = temp


def fold():
    w, h, cur = N//2, 1, 0

    for _ in range(2):
        temp = []
        for i in range(h):
            for j in range(w):
                r, c = N - h + i, cur + j
                temp.append(tank[r][c])
                tank[r][c] = 0
        for i in range(h):
            for j in range(w):
                r, c = N-1-h-i, N-1-j
                tank[r][c] = temp.pop(0)
        cur += w
        w //= 2
        h *= 2


cnt = 0
while get_max_min_diff() > K:

    add_fish()

    stack()
    adjust()
    unstack()

    fold()
    adjust()
    unstack()
    cnt += 1

print(cnt)
