import math
import sys

input = sys.stdin.readline
# lazy propagation
# 세그먼트 트리를 이용하여 범위에 더해져야 가는 값을 기록해 두고
# 루트 노드에서 목표 노드(K) 까지 이동하면서 세그먼트에 기록되어 있는 값을 더해주는 방식


def update(i, s, e, a, b, k):
    if b < s or e < a:
        return
    if a <= s and e <= b:
        tree[i] += k
        return
    m = (s + e) // 2
    update(i*2, s, m, a, b, k)
    update(i*2+1, m+1, e, a, b, k)


def getK(i, s, e, k):
    if k < s or e < k:
        return 0
    if s == e:
        return tree[i]
    if s <= k and k <= e:
        m = (s + e) // 2
        return tree[i] + getK(i*2, s, m, k) + getK(i*2+1, m+1, e, k)


N = int(input())
A = [*map(int, input().split())]
n = math.ceil(math.log2(N)) + 1
n = 1 << n
tree = [0] * n

for _ in range(int(input())):
    q, *l = map(int, input().split())
    if q == 1:
        a, b, k = l
        update(1, 0, N-1, a-1, b-1, k)
    elif q == 2:
        k = l.pop()
        print(getK(1, 0, N-1, k-1) + A[k-1])
