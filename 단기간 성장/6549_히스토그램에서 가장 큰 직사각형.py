import sys

# 1. 분할 정복 (세그먼트 트리)
sys.setrecursionlimit(10**6)
from math import ceil, log2

def init(node, s, e):
    if s == e:
        tree[node] = s
        return s
    m = (s+e)//2
    i_l = init(node*2, s, m)
    i_r = init(node*2+1, m+1, e)
    tree[node] = i_l if H[i_l] <= H[i_r] else i_r
    return tree[node]


def query(node, s, e, l, r):
    if l > e or r < s:
        return -1
    if l <= s and e <= r:
        return tree[node]
    m = (s+e)//2
    i_l = query(node*2, s, m, l, r)
    i_r = query(node*2+1, m+1, e, l, r)
    if i_l < 0:
        return i_r
    elif i_r < 0:
        return i_l
    else:
        return i_l if H[i_l] < H[i_r] else i_r


def solve(s, e):
    if s > e:
        return 0
    idx = query(1, 0, N-1, s, e)
    area = H[idx] * (e - s + 1)
    area = max(area, solve(s, idx-1), solve(idx+1, e))
    return area


while True:
    H = [*map(int, input().split())]
    N = H.pop(0)
    if N == 0: break
    n = ceil(log2(N)) + 1
    n = 1 << n
    tree = [0] * n
    init(1, 0, N-1)
    print(solve(0, N-1))

# 2. Stack
def get_area():
    stack = []
    ans = 0
    for i in range(N):
        while stack and H[stack[-1]] >= H[i]:
            h = H[stack.pop()]
            w = i - stack[-1] - 1 if stack else i
            ans = max(ans, h * w)
        stack.append(i)

    while stack:
        h = H[stack.pop()]
        w = N - stack[-1] - 1 if stack else N
        ans = max(ans, h * w)
    return ans


while True:
    H = [*map(int, input().split())]
    N = H.pop(0)
    if N == 0: break
    print(get_area())
