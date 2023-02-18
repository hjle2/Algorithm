# 1번, 2번 집 색은 다르다
# n번 , n-1번 집 색은 다르다
# i번 집은 i-1, i+1 집 색과 다르다

N = int(input())
cost = [[*map(int, input().split())]for _ in range(N)]
for i in range(1, N):
    for j in range(3):
        cost[i][j] += min(cost[i-1][d] if j != d else 1e9 for d in range(3))
print(min(cost[-1]))