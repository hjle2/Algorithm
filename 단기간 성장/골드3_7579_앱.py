# 활성화 : 보이지 않더라도 직전의 상태가 메인 메모리에 기록되어 있는 것
# 다시 실행할 때 직전의 상태를 읽어들여 실행 준비를 빠르게 하기 위하여
# 메모리가 제한적이기 때문에 비활성화 해야한다
# 비활성화 한 후에 다시 실행할 경우 추가적인 비용 C
# 추가로 M바이트가 필요한 앱을 실행할 때 비용을 최소화하여 메모리를 확보하는 방법을 찾는다

N, M = map(int, input().split())
mem = [0] + [*map(int, input().split())]
cost = [0] + [*map(int, input().split())]
total = sum(cost)
dp = [[0] * (N+1) for _ in range(total+1)]
# 열 = 비용, 행 = 비용
for i in range(total+1):
    for j in range(1, N+1):
        if i >= cost[j]:
            dp[i][j] = max(dp[i][j-1], dp[i-cost[j]][j-1] + mem[j])
        else:
            dp[i][j] = dp[i][j-1]
        if dp[i][j] >= M:
            print(i)
            exit()
print(total)