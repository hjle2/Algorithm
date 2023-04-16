# 1km당 1L
# 마을에 도착하지 못할 경우 -1
# 주유소의 개수 n
import heapq
n = int(input())

station = []
for i in range(n):
    a, b = map(int, input().split())
    station.append([a, b])
station.sort()
arrival, gas = map(int, input().split())
station.append([arrival, 0])
que = []
ans = 0
prv = 0
for i in range(n+1):
    cur, add_gas = station[i]

    while cur - prv > gas: # 현재 주유소에 도달할 수 없었다면
        ans += 1
        if not que:  # 오는 길에 충분한 주유소가 없엇때만 답은 -1
            ans = -1
            break
        gas -= heapq.heappop(que)

    if ans == -1: break
    # 오는 길에 충전 다 했으면
    heapq.heappush(que, -add_gas)
    gas -= cur - prv
    prv = cur

print(ans)
