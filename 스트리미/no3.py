ans = 10**5
def dfs(ar, i, a, b):
    global ans
    n = len(ar)
    while i<n and ar[i]:
        i += 1
    if i == n:
        for j in range(1, 10 ** 5):
            if j not in ar:
                ans = min(ans, j)
                return
    if ar[i] == 0:
        ar[i] = a[i]
        dfs(ar, i + 1, a, b)
        ar[i] = b[i]
        dfs(ar, i + 1, a, b)
        ar[i] = 0

def sol(a, b):
    n = len(a)
    ar = [0] * n
    for i in range(n):
        if a[i] == b[i]:
            ar[i] = a[i]
    dfs(ar, 0, a, b)
    return ans
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(sol(a, b))