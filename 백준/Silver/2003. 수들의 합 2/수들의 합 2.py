n, m = map(int, input().split())
ar = [*map(int, input().split())]

ans, sum, j = 0, 0, 0
for i in range(n):      # 두 포인터 i, j로 구간합을 탐색한다
    while j < n and sum < m:
        sum += ar[j]
        j += 1
    if sum == m:
        ans += 1
    sum -= ar[i]        # sum에서 ar[i]를 빼주고, i+1 ~ j 구간합에서부터 이어서 계산한다.
print(ans)
