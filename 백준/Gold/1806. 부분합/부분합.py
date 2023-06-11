n, s = map(int, input().split())
ar = [*map(int, input().split())]

sum, min_len, j = 0, 1e9, 0       # i, j 두 포인터로 누적합을 계산
for i in range(n):
    while j < n and sum < s:    # j가 index범위내에 있고, s보다 작을때만 누적합을 구함
        sum += ar[j]
        j += 1
    if sum >= s:                # sum이 s 이상이면, 부분합 배열의 개수를 갱신
        min_len = min(min_len, j - i)
    sum -= ar[i]
print(min_len if min_len != 1e9 else 0)

