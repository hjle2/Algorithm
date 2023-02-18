import math
import sys
input = sys.stdin.readline


def init(i, s, e):
    if s == e:
        tree[i] = (s, s)
        return
    m = (s + e) // 2
    init(i*2, s, m)
    init(i*2+1, m+1, e)
    tree[i] = (min(tree[i*2][0], tree[i*2+1][0]), max(tree[i*2][1], tree[i*2+1][1]))


def update(i, s, e, idx, v):
    if idx > e or idx < s:
        return
    if s == e:
        tree[i] = (v, v)
        return
    m = (s + e) // 2
    update(i*2, s, m, idx, v)
    update(i*2+1, m+1, e, idx, v)
    tree[i] = (min(tree[i*2][0], tree[i*2+1][0]), max(tree[i*2][1], tree[i*2+1][1]))


def interval_m(i, s, e, a, b):
    if b < s or a > e:
        return True
    if a <= s and b >= e:
        return a <= tree[i][0] and b >= tree[i][1]
    m = (s + e) // 2
    return interval_m(i*2, s, m, a, b) and interval_m(i*2+1, m+1, e, a, b)


for _ in range(int(input())):
    N, K = map(int, input().split())
    n = math.ceil(math.log2(N)) + 1
    n = 1 << n
    tree = [(0, 0)] * n
    A = [i for i in range(N)]
    init(1, 0, N-1)

    for _ in range(K):
        q, a, b = map(int, input().split())
        if q:
            flag = interval_m(1, 0, N-1, a, b)
            print(['NO', 'YES'][flag])
        else:
            A[a], A[b] = A[b], A[a]
            update(1, 0, N-1, a, A[a])
            update(1, 0, N-1, b, A[b])

