import sys
from math import ceil, log2

input = sys.stdin.readline

def init(i, s, e):
    if s == e:
        tree[i] = A[s]
        return
    m = (s+e)//2
    init(i*2, s, m)
    init(i*2+1, m+1, e)
    tree[i] = tree[i*2] * tree[i*2+1]


def update(i, s, e, idx, v):
    if s > idx or e < idx:
        return
    if s == e:
        tree[i] = v
        return
    m = (s+e)//2
    update(i*2, s, m, idx, v)
    update(i*2+1, m+1, e, idx, v)
    tree[i] = tree[i*2] * tree[i*2+1]


def interval_mult(i, s, e, l, r):
    if s > r or e < l:
        return 1
    if l <= s and e <= r:
        return tree[i]
    m = (s+e)//2
    return interval_mult(i*2, s, m, l, r) * interval_mult(i*2+1, m+1, e, l, r)


N, M, K = map(int, input().split())
A = [int(input())for _ in range(N)]
n = ceil(log2(N)) + 1
n = 1 << n
tree = [0]*n
init(1, 0, N-1)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 0, N-1, b-1, c)
    else:
        print(interval_mult(1, 0, N-1, b-1, c-1))
