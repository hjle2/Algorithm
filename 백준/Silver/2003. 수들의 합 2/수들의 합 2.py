n, m = map(int, input().split())
ar = list(map(int, input().split()))

ans = 0
sum = 0
end = 0

for i in range(n):
    while sum < m and end < n:  # 구간합이 m보다 작을 동안, end가 인덱스 범위내에 있을 동안만 반복
        sum += ar[end]          # 구간합 구하기
        end += 1                # 인덱스 증가시키기
    if sum == m:
        ans += 1
    sum -= ar[i]                # 다음 i부터 구간합을 구하기위해 현재 값은 빼준다
print(ans)
