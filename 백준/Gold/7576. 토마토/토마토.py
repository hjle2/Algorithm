import copy

m, n = map(int, input().split())
box = [[*map(int, input().split())]for _ in range(n)]

tomato = []
minus_cnt = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            tomato.append((i, j))
        if box[i][j] == -1:
            minus_cnt+=1


def get_cnt(tomato):
    cnt = 0
    tmp = []
    for x, y in tomato:
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = x + dx, y + dy
            if 0 <= nr < n and 0 <= nc < m and box[nr][nc] == 0:
                box[nr][nc] = 1
                cnt += 1
                tmp.append((nr, nc))
    return cnt, tmp

ans = 0
total = 0
while True:
    cnt, tomato = get_cnt(tomato)
    total += cnt
    if cnt == 0:
        break
    ans += 1

for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            ans = -1
            break
    if ans == -1:
        break
print(ans)