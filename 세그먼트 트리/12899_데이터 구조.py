import sys
from math import ceil, log2

input = sys.stdin.readline

def add(v):
    i = n + v - 1
    while i >= 1:
        tree[i] += 1
        i //= 2


def remove(q):
    i = 1
    while i < n:
        if tree[i*2] < q:
            q -= tree[i*2]
            i = i*2+1
        else:
            i *= 2
    print(i - n + 1)
    while i >= 1:
        tree[i] -= 1
        i //= 2


n = 2 * 10 ** 6
n = ceil(log2(n))
n = 1 << n
tree = [0] * (n*2)

for _ in range(int(input())):
    t, x = map(int, input().split())
    if t == 1:
        add(x)
    else:
        remove(x)