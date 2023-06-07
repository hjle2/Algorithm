# 현재 활성화되어 있는 앱의 수 n
# 새로운 앱 B를 실행하기위해 필요한 메모리 m 바이트
n, m = map(int, input().split())

# 현재 활성화되어 있는 앱이 사용중인 메모리의 바이트 수
a = [*map(int, input().split())]
# 각 앱을 비활성화 했을 경우의 비용
c = [*map(int, input().split())]
# i번째까지 앱을 고려하였을 때 j비용이 되는 확보된 메모리의 수
C = sum(c)
dp = [[0] * (C+1) for _ in range(n+1)]

flag = 0
# i번째 앱까지 고려
for j in range(C+1):
    for i in range(1, n+1):
        # j비용이 되는 메모리의 수를 구한다
        app_byte = a[i-1]
        app_cost = c[i-1]
        # 현재 앱의 비용보다 크면 앱을 비활성화 시킴
        if j-app_cost >= 0: dp[i][j] = dp[i-1][j-app_cost] + app_byte
        dp[i][j] = max(dp[i][j], dp[i-1][j])
        if dp[i][j] >= m:
            flag = j
            break
    if flag:
        break
print(flag)
