import sys
from math import ceil, log2

input = sys.stdin.readline


def init(i, s, e):
    if s == e:
        tree[i] = [A[s], A[s]]
        return
    m = (s+e)//2
    init(i*2, s, m)
    init(i*2+1, m+1, e)
    tree[i] = [min(tree[i*2][0], tree[i*2+1][0]), max(tree[i*2][1], tree[i*2+1][1])]


def interval(i, s, e, l, r):
    if s > r or e < l:
        return [tree[1][1], tree[1][0]]
    if l <= s and e <= r:
        return tree[i]
    m = (s+e)//2
    tmp1 = interval(i * 2, s, m, l, r)
    tmp2 = interval(i*2+1, m+1, e, l, r)
    return [min(tmp1[0], tmp2[0]), max(tmp1[1], tmp2[1])]


N, M = map(int, input().split())
A = [int(input())for _ in range(N)]
n = ceil(log2(N)) + 1
n = 1 << n
tree = [(0, 0)]*n
init(1, 0, N-1)

for _ in range(M):
    a, b = map(int, input().split())
    print(*interval(1, 0, N-1, a-1, b-1))
