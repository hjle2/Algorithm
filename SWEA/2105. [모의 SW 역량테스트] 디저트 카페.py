# 대각선 방향으로 움직이고,
# 사각형 모양을 그려 출발한 카페로 돌아와야 한다
# 같은 숫자가 있으면 안된다.
# 하나만 가는 것도 안된다.
# 다시 되돌아 가는 것도 안된다.
# 최대한 많이 먹는 경우 리턴
# 없으면 -1
dr = [1, 1, -1, -1]
dc = [-1, 1, -1, 1]

def get_lr(i, j):
    r, c = i, j
    l_c = r_c = 0
    while 0<=r<n and 0<=c<n:
        r, c = r+1, c-1
        l_c += 1
    r, c = i, j
    while 0<=r<n and 0<=c<n:
        r, c = r+1, c+1
        r_c += 1
    return l_c-1, r_c-1

def getdist(i, j, l_c, r_c):
    q = [a[i][j]]
    r, c = i, j
    for _ in range(l_c):
        r, c = r + 1, c - 1
        if not 0<=r<n or not 0<=c<n: return 0
        if a[r][c] not in q:
            q.append(a[r][c])
        else: return 0
    for _ in range(r_c):
        r, c = r + 1, c + 1
        if not 0<=r<n or not 0<=c<n: return 0
        if a[r][c] not in q:
            q.append(a[r][c])
        else:return 0
    for _ in range(l_c):
        r, c = r - 1, c + 1
        if not 0<=r<n or not 0<=c<n: return 0
        if a[r][c] not in q:
            q.append(a[r][c])
        else:return 0
    for _ in range(r_c-1):
        r, c = r - 1, c - 1
        if not 0<=r<n or not 0<=c<n: return 0
        if a[r][c] not in q:
            q.append(a[r][c])
        else:return 0
    return len(q)


def caldist(i, j, l_c, r_c):
    ans = 0
    for l in range(l_c):
        for r in range(r_c):
            ans = max(ans, getdist(i, j, l+1, r+1))
    return ans



def sol():
    ans = 0
    for r in range(n-2):
        for c in range(1, n-1):
            l_c, r_c = get_lr(r, c)
            ans = max(ans, caldist(r, c, l_c, r_c))
    return ans if ans > 0 else -1

for t in range(int(input())):
    n = int(input())
    a = [list(map(int, input().split()))for _ in range(n)]
    print(f'#{t+1}', sol())




