n = int(input())
k = int(input())

l, r = 1, k
while l <= r:
    m = (l + r) // 2
    
    tmp = 0
    for i in range(1, n+1):
        tmp += min(m // i, n)
    
    if tmp < k:
        l = m + 1
    else:
        ans = m
        r = m - 1
print(ans)