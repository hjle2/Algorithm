import sys
input = sys.stdin.readline

def flip(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1-A[i][j]


def equal():
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                return False
    return True


N, M = map(int, input().split())
A = [[*map(int, [*input()][:-1])]for _ in range(N)]
B = [[*map(int, [*input()][:-1])]for _ in range(N)]
cnt = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            cnt += 1
            flip(i, j)

print(cnt if equal() else -1)