n, c = map(int, input().split())
ar = [*map(int, input().split())]
a_ar = ar[:n//2]
b_ar = ar[n//2:]
a_sum = []
b_sum = []


def dfs(w_ar, s_ar, l, w):
    if l >= len(w_ar):
        s_ar.append(w)
        return
    dfs(w_ar, s_ar, l+1, w)
    dfs(w_ar, s_ar, l+1, w + w_ar[l])


def binary_search(ar, target, l, r):
    while l < r:
        m = (l + r) // 2
        if ar[m] <= target:
            l = m + 1
        else:
            r = m
    return r


dfs(a_ar, a_sum, 0, 0)
dfs(b_ar, b_sum, 0, 0)
b_sum.sort()

cnt = 0
for i in a_sum:
    if c < i:
        continue
    cnt += binary_search(b_sum, c-i, 0, len(b_sum))
print(cnt)