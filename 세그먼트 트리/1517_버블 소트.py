def merge_sort(s, e):
    if s >= e:
        return 0
    m = (s+e)//2
    ans = merge_sort(s, m) + merge_sort(m+1, e)

    l, r = s, m+1
    tmp = []
    while l <= m and r <= e:
        if A[l] <= A[r]:
            tmp.append(A[l])
            l += 1
        else:
            tmp.append(A[r])
            r += 1
            ans += m - l + 1
    if l <= m:
        tmp += A[l:m+1]
    if r <= e:
        tmp += A[r:e+1]
    for i, v in enumerate(tmp):
        A[s+i] = v
    return ans


N = int(input())
A = [*map(int, input().split())]
print(merge_sort(0, N-1))
