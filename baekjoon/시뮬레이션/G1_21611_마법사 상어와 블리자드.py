# N 은 항상 홀수
# 상어는 중앙에
# 4가지 방향 ↑, ↓, ←, →
# 1, 2, 3, 4
# si 이하인 모든 칸에 얼음 파편을 던져 그 칸에 있는 구슬을 모두 파괴

N, M = map(int, input().split())
A = [[*map(int, input().split())]for _ in range(N)]
m = (N + 1) // 2 - 1

link = []
mark = [[0] * N for _ in range(N)]
boom1, boom2, boom3 = 0, 0, 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

mdx = [0, 1, 0, -1]
mdy = [-1, 0, 1, 0]

def change():
    global link
    if not link:
        return

    before, cnt = link[0], 0
    total = 0
    new_link = []
    for idx, v in enumerate(link):
        if v == before:
            cnt += 1
        else:
            new_link.append(cnt)
            new_link.append(before)
            total += 2
            if total == N * N - 1:
                break
            before, cnt = v, 1

    if total < N * N - 1:
        new_link.append(cnt)
        new_link.append(before)

    link = new_link


def remove_yeonsok():
    global boom1, boom2, boom3
    remove_index = []
    before, cnt = 0, 0
    for i, v in enumerate(link):
        if v == before:
            cnt += 1
        else:
            if cnt >= 4:
                remove_index.insert(0, (i - cnt, cnt))
            before = v
            cnt = 1
    if cnt >= 4:
        remove_index.insert(0, (i - cnt, cnt))

    if not remove_index:
        return False
    else:
        for idx , cnt in remove_index:
            if link[idx] == 1:
                boom1 += cnt
            elif link[idx] == 2:
                boom2 += cnt
            elif link[idx] == 3:
                boom3 += cnt
            for _ in range(cnt):
                link.pop(idx)
        return True


def make_index():
    x, y = m, m
    l = 1
    idx = 1

    while 0 <= x < N and 0 <= y < N:
        isEnd = False
        for d in range(4):
            for _ in range([l, l+1][d > 1]):
                x, y = x + mdx[d], y + mdy[d]
                if y < 0:
                    isEnd = True
                    break
                mark[x][y] = idx
                if A[x][y] > 0:
                    link.append(A[x][y])
                idx += 1
            if isEnd:
                break
        if isEnd: break
        l += 2


make_index()

for _ in range(M):
    # direction, distance
    d, s = map(int, input().split())
    x, y = m, m
    toBreak = []
    # 구슬 부수기
    for _ in range(s):
        x, y = x + dx[d-1], y + dy[d-1]
        if x < 0 or y < 0 or x >= N or y >= N: break
        idx = mark[x][y]
        if idx > 0:
            toBreak.append(idx-1)
    while toBreak:
        idx = toBreak.pop()
        if len(link) > idx:
            link.pop(idx)

    # 연속하는 구슬 폭발
    flag = True
    while flag:
        flag = remove_yeonsok()

    # 구슬 변화
    change()



print(boom1 + boom2 * 2 + boom3 * 3)


