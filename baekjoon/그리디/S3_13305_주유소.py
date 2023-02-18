# 어떤 나라에 N개의 도시가 있다
# 이 도시는 일직선 위에 있다
# 처음 출발할 때 주유소에서 기름을 넣고 출발한다
# 얼마든지 기름을 넣을 수 있고
# 도로를 이동할 때마다 1리터의 기름을 사용한다
# 각 도시에는 단 하나의 주유소가 있고 리터당 가격은 다를 수 있다
# 처음도시에서 끝 도시로 이동하는 최소의 비용을 구하라

import sys
input = sys.stdin.readline
N = int(input())
R = [*map(int, input().split())]
P = [*map(int, input().split())]
del P[-1]
for i in range(N-1):
    P[i] = [i, P[i]]
P.sort(key=lambda x:x[1])
ans = 0
idx = N
for pi, p in P:
    if idx < pi: continue
    ans += p * sum(R[pi:idx])
    idx = pi
print(ans)
# 주유소의 가격이 가장 싼 위치에 도착하면 이후 가야하는 거리의 합만큼 주유한다
# 그 다음 가격이 싼 위치에 도착, 이미 더 싼 주유소에서 주유한 경우라면 패스
# 아니라면 가장 싼 주유소를 만나기 전까지 가야하는 거리의 합만큼 주유!
