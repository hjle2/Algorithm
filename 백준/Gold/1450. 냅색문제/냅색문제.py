n, c = map(int, input().split())
ar = [*map(int, input().split())]
a_ar = ar[:n//2]
b_ar = ar[n//2:]
a_sum = []
b_sum = []

# 이분 탐색으로 모든 합의 경우를 구하기
def dfs(w_ar, s_ar, l, w):
    if l >= len(w_ar):
        s_ar.append(w)
        return
    dfs(w_ar, s_ar, l+1, w)
    dfs(w_ar, s_ar, l+1, w + w_ar[l])

# 이분 탐색으로 가방에 넣을 수 있는 경우의 수 구하기
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
