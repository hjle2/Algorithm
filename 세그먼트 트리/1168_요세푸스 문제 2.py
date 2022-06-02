import sys


input = sys.stdin.readline


def init():
    tree[n:n+N] = [1]*N
    for i in range(n-1, 0, -1):
        tree[i] = tree[i*2] + tree[i*2]


def update(i, v):
    i += n
    tree[i] = v
    i //= 2
    while i >= 1:
        tree[i] = tree[i*2] + tree[i*2+1]
        i //= 2


def query(k):
    i = 1
    while k:
        # 여기서 i-n ? i+1-n?
        if i*2 >= n*2:
            if tree[i]:
                return i-n
            else:
                return i+1-n
        if tree[i*2] <= k:
            k -= tree[i*2]
            i = i*2+1
        else:
            i *= 2
    return i-n


N, K = map(int, input().split())
# bit_length?
n = 1 << N.bit_length()
tree = [0] * (n * 2)
init()
ans = []
p = K
# 역순으로 진행하는 이유는?
for i in range(N, 0, -1):
    idx = query(p)
    update(idx, 0)
    ans.append(str(idx+1))
    if i != 1:
        p = (p+K-1) % (i-1)
    else:
        p = p+K-1
    if not p:
        p = i-1

print(f"<{','.join(ans)}>")


