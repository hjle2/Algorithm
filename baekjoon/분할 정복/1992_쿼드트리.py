# 흑백 영상을 압축하여 표현하는 데이터 구조
# 주어진 영상이 모두 0으로 되어 있으면 0, 1로 되어 있으면 1
# 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래 4개의 영상으로 나누어 압축

def isall(pt, size):
    x, y = pt
    v = A[x][y]
    for i in range(size):
        for j in range(size):
            if A[x + i][y + j] != v:
                return False
    return True


def solve(pt, size):
    ret = '('
    x, y = pt
    for dx, dy in d:
        nx, ny = x + dx*size, y + dy*size
        if not isall((nx, ny), size):
            ret += solve((nx, ny), size//2)
        else:
            ret += str(A[nx][ny])
    return ret + ')'


# N은 2의 제곱수, 1<=N<=64
d = [(0, 0), (0, 1), (1, 0), (1, 1)]
N = int(input())
A = [[*map(int, [*input()])]for _ in range(N)]
if isall((0, 0), N):
    print(A[0][0])
else:
    print(solve((0, 0), N//2))
