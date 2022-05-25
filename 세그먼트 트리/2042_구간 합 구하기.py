# M 수 변경이 일어나는 횟수
# K 구간의 합을 구하는 횟수
# a가 1인 경우 b(1 ≤ b ≤ N)번째 수를 c로 swap
# a가 2인 경우에는 b(1 ≤ b ≤ N)번째 수부터 c(b ≤ c ≤ N)번째 수까지의 합
import math
import sys

input = sys.stdin.readline

# 세그먼트 트리
# 트리 배열 크기는 배열의 갯수 N보다 큰 수중에 가장 가까운 수의 제곱의 2배로 할당
# 1 << log2(len(ar)) + 1
def init(now, frm, to):
    if frm == to:
        tree[now] = A[frm]
        return A[frm]
    mid = (frm + to) // 2
    tree[now] = init(now*2, frm, mid) + init(now*2+1, mid+1, to)
    return tree[now]


def getsum(now, s, e, frm, to):
    if s > to or e < frm:
        return 0
    if s >= frm and e <= to:
        return tree[now]
    mid = (s + e) // 2
    return getsum(now*2, s, mid, frm, to) + getsum(now*2+1, mid+1, e, frm, to)


def update(now, s, e, idx, v):
    if idx < s or idx > e:
        return tree[now]
    if s == e:
        tree[now] = v
        return v
    mid = (s + e) // 2
    tree[now] = update(now*2, s, mid, idx, v) + update(now*2+1, mid+1, e, idx, v)
    return tree[now]

N, M, K = map(int, input().split())
A = [int(input())for _ in range(N)]
# 세그먼트의 크기 설정
# 배열의 개수가 N 이면,
# N보다 큰 가장 가까운 수의 제곱수의 2배(+1)
n = math.ceil(math.log2(len(A))) + 1
n = 1 << n
tree = [0] * n
init(1, 0, N-1)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 0, N-1, b-1, c)
    elif a == 2:
        print(getsum(1, 0, N-1, b-1, c-1))
