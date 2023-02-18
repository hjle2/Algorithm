# 보드의 크기와 보드판의 블록 상태가 주어졌을 때, 최대 5번 이동해서 만들 수 있는 가장 큰 블록 값을 구하라
import sys
from copy import deepcopy

input = sys.stdin.readline

def drag(A, d):
    # l / r
    if d < 2:
        frm, to, d = (0, N, 1) if d == 0 else (N-1, -1, -1)
        for i in range(N):
            c, x = frm, -1
            for j in range(frm, to, d):
                if A[i][j] == 0:
                    continue
                if x == -1:
                    x = A[i][j]
                    continue
                if x == A[i][j]:
                    A[i][c], x = x * 2, -1
                    c += d
                else:
                    A[i][c], x = x, A[i][j]
                    c += d
            if x != -1:
                A[i][c] = x
                c += d
            for j in range(c, to, d):
                A[i][j] = 0

    else:
        frm, to, d = (0, N, 1) if d == 2 else (N-1, -1, -1)
        for i in range(N):
            c, x = frm, -1
            for j in range(frm, to, d):
                if A[j][i] == 0:
                    continue
                if x == -1:
                    x = A[j][i]
                    continue
                if x == A[j][i]:
                    A[c][i], x = x * 2, -1
                    c += d
                else:
                    A[c][i], x = x, A[j][i]
                    c += d
            if x != -1:
                A[c][i] = x
                c += d
            for j in range(c, to, d):
                A[j][i] = 0

def dfs(A, cnt, ans):
    ans = max(ans, max(max(A[i])for i in range(N)))
    if cnt == 0:
        return ans
    ret = 0
    for d in range(4):
        ar = deepcopy(A)
        drag(ar, d)
        ret = max(ret, dfs(ar, cnt-1, ans))
    return ret

N = int(input())
A = [[*map(int, input().split())]for _ in range(N)]
print(dfs(A, 5, 0))