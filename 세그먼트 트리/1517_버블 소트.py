def merge_sort(s, e):
    if s >= e:
        return 0
    mid = (s + e) // 2
    cnt = merge_sort(s, mid) + merge_sort(mid+1, e)

    a, b = s, mid+1
    tmp = []
    while a <= mid and b <= e:
        if A[a] <= A[b]:
            tmp.append(A[a])
            a += 1
        else:
            tmp.append(A[b])
            b += 1
            cnt += (mid - a + 1)
    if a <= mid:
        tmp += A[a:mid+1]
    if b <= e:
        tmp += A[b:e+1]
    for i in range(len(tmp)):
        A[s+i] = tmp[i]
    return cnt

N = int(input())
A = [*map(int, input().split())]
print(merge_sort(0, N-1))