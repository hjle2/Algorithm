# 한 쪽 문에서 다른 쪽 문을 볼 수 있도록?
# 거울은 대각성 방향으로 설치
# 양면 거울이기 때문에 양쪽 반사

# 0 <-> 1
# 2 <-> 3
import sys
input = sys.stdin.readline
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
otherD = [1, 0, 3, 2]
def getDirection(i, j, x, y):
    if i == x:
        return 0
    elif j == y:
        return 2


def getOtherMirrors(x, y, d):
    ans = []
    dx, dy = dir[d]
    i, j = x, y
    while True:
        x += dx; y += dy
        if 0<=x<N and 0<=y<N:
            if ar[x][y] == '!' or ar[x][y] == '#':
                ans.append((x, y, getDirection(i, j, x, y)))
            elif ar[x][y] == '*':
                break
        else:
            break
    return ans


def bfs():
    i, j = door[0]
    visited = [[0]*N for _ in range(N)]
    que = []
    for d in range(4):
        que.append((i, j, 0, d))
    visited[i][j] = 1
    while que:
        r, c, cnt, d = que.pop(0)
        mir = getOtherMirrors(r, c, d)
        for i, j, dr in mir:
            if not visited[i][j]:
                visited[i][j] = True
                if ar[i][j] == '#':
                    return cnt
                que.append((i, j, cnt+1, dr))
                que.append((i, j, cnt+1, otherD[dr]))


N = int(input())
ar = []
door = []
mirror = []
for i in range(N):
    tmp = [*input()]
    for j in range(N):
        if tmp[j] == '#': door.append((i, j))
        elif tmp[j] == '!': mirror.append((i, j))
    ar.append(tmp)
print(bfs())
# 3
# ##!
# !!!
# !!!
