# 세그먼트 트리 활용 문제

import math
import sys

# 세그먼트 트리 생성
def init(now, s, e):
    if s == e:
        tree[now] = A[s]
        return A[s]
    mid = (s + e) // 2
    tree[now] = init(now*2, s, mid) + init(now*2+1, mid+1, e)
    return tree[now]


# 세그 먼트 트리 데이터 수정
def update(now, s, e, idx, v):
    if s > idx or e < idx:
        return tree[now]
    if s == e:
        tree[now] = v
        return v
    mid = (s + e) // 2
    tree[now] = update(now*2, s, mid, idx, v) + update(now*2+1, mid+1, e, idx, v)
    return tree[now]

# 세그먼트 트리의 구간 합
def interval_sum(now, s, e, frm, to):
    if s > to or e < frm:
        return 0
    if s >= frm and e <= to:
        return tree[now]
    mid = (s + e) // 2
    return interval_sum(now*2, s, mid, frm, to) + interval_sum(now*2+1, mid+1, e, frm, to)


input = sys.stdin.readline
N, M, K = map(int, input().split())
A = [int(input())for _ in range(N)]
# 세그먼트 트리의 크기
# 배열의 갯수 N 보다 큰 수 중 가장 가까운 수의 제곱수 * 2
n = math.ceil(math.log2(N)) + 1
n = 1 << n
tree = [0] * n
init(1, 0, N-1)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 0, N-1, b-1, c)
    elif a == 2:
        print(interval_sum(1, 0, N-1, b-1, c-1))
