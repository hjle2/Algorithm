# 같은 수로 되어 있다면 종이를 사용
# 아닌 경우 종이를 같은 크기의 종이 9개로 자르고, 잘린 종이에 해 다시 반복

# N 1<=N<=3**7 N 은 3**k꼴
def all(pt, size):
    if size == 1:
        return True
    x, y = pt
    v = A[x][y]
    for i in range(size):
        for j in range(size):
            if A[i+x][j+y] != v:
                return False
    return True


def solve(pt, size):
    x, y = pt
    if all(pt, size):
        ans[A[x][y]+1] += 1
    else:
        size //= 3
        for i in range(3):
            for j in range(3):
                nx, ny = x + i*size, y + j*size
                solve((nx, ny), size)


N = int(input())
A = [[*map(int, input().split())]for _ in range(N)]
ans = [0] * 3
solve((0, 0), N)
print(*ans, sep='\n')