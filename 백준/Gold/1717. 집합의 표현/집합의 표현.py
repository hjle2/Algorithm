import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def union(a, b):
    a_p = get_parent(a)
    b_p = get_parent(b)
    if a_p > b_p:
        a_p, b_p = b_p, a_p
    parent[b_p] = a_p


def get_parent(a):
    if parent[a] == a:
        return a
    parent[a] = get_parent(parent[a])
    return parent[a]


n, m = map(int, input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    op, a, b = map(int, input().split())
    if op:
        print('YES' if get_parent(a) == get_parent(b) else 'NO')
    else:
        union(a, b)