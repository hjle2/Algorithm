n = int(input())
ar = sorted([*map(int, input().split())])

l, r = 0, n-1                   # 투 포인터로 쓸 왼쪽, 오른쪽 포인터
min_diff = abs(ar[l] + ar[r])   # 두 용액의 특성값 최소 값
ans = [ar[l], ar[r]]            # 최소값의

while l < r:
    tmp = ar[l] + ar[r]         # 두 용액의 특성값
    if abs(tmp) < min_diff:     # 최소 특성값보다 작다면, 갱신해준다.
        min_diff = abs(tmp)
        ans = [ar[l], ar[r]]
        if min_diff == 0:       # 특성값이 0이라면 더이상 탐색하지 않아도 된다.
            break

    if tmp < 0:                 # 특성값이 음수라면 특성값이 증가될 수 있도록 왼쪽 포인터를 증가시킨다.
        l += 1
    else:                       # 특성값이 양수라면 특성값이 감소될 수 있도록 오른쪽 포인터를 감소시킨다.
        r -= 1
print(*sorted(ans))