n = int(input())
ar = [*map(int, input().split())]
m = int(input())

def calc(budget):
    ret = 0
    for num in ar:
        ret += min(num, budget)
    return ret


ar.sort()
ans = ar[0]
l, r = 0, ar[-1]
while l <= r:
    mid = (l + r) // 2
    v = calc(mid)
    if v <= m:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)