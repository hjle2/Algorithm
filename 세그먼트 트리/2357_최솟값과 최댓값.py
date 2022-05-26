import math
import sys

input = sys.stdin.readline

# flag min 인지, max 인지
# max = True, min = False
def init_min(now, s, e):
    if s == e:
        tree_min[now] = A[s]
        return A[s]
    mid = (s + e) // 2
    tree_min[now] = min(init_min(now*2, s, mid), init_min(now*2+1, mid+1, e))
    return tree_min[now]


def init_max(now, s, e):
    if s == e:
        tree_max[now] = A[s]
        return A[s]
    mid = (s + e) // 2
    tree_max[now] = max(init_max(now*2, s, mid), init_max(now*2+1, mid+1, e))
    return tree_max[now]



def interval_min(now, s, e, frm, to):
    if frm > e or to < s:
        return tree_max[1]
    if frm <= s and to >= e:
        return tree_min[now]
    mid = (s + e) // 2
    return min(interval_min(now*2, s, mid, frm, to), interval_min(now*2+1, mid+1, e, frm, to))


def interval_max(now, s, e, frm, to):
    if frm > e or to < s:
        return 0
    if frm <= s and to >= e:
        return tree_max[now]
    mid = (s + e) // 2
    return max(interval_max(now*2, s, mid, frm, to), interval_max(now*2+1, mid+1, e, frm, to))


N, M = map(int, input().split())
A = [int(input())for _ in range(N)]
n = math.ceil(math.log2(N)) + 1
n = 1 << n
tree_min = [0] * n
tree_max = [0] * n
init_min(1, 0, N-1)
init_max(1, 0, N-1)

for _ in range(M):
    a, b = map(int, input().split())
    print(interval_min(1, 0, N-1, a-1, b-1), interval_max(1, 0, N-1, a-1, b-1))
