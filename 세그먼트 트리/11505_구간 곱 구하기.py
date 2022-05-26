import math
import sys

input = sys.stdin.readline


def init(now, s, e):
    if s == e:
        tree[now] = A[s]
        return A[s] % p
    mid = (s + e) // 2
    tree[now] = init(now*2, s, mid) * init(now*2+1, mid+1, e) % p
    return tree[now]


def update(now, s, e, idx, v):
    if s > idx or e < idx:
        return tree[now]
    if s == e:
        tree[now] = v % p
        return tree[now]
    mid = (s + e) // 2
    tree[now] = update(now*2, s, mid, idx, v) * update(now*2+1, mid+1, e, idx, v) % p
    return tree[now]


def interval_mult(now, s, e, frm, to):
    if to < s or frm > e:
        return 1
    if frm <= s and to >= e:
        return tree[now]
    mid = (s + e) // 2
    return interval_mult(now*2, s, mid, frm, to) * interval_mult(now*2+1, mid+1, e, frm, to) % p


p = 1000000007
N, M, K = map(int, input().split())
A = [int(input())for _ in range(N)]
n = math.ceil(math.log2(N)) + 1
n = 1 << n
tree = [0] * n
init(1, 0, N-1)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 0, N-1, b-1, c)
    elif a == 2:
        print(interval_mult(1, 0, N-1, b-1, c-1))
