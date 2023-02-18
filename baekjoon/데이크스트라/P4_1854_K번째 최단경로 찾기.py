import sys; import heapq
input = sys.stdin.readline
INF = sys.maxsize
def dijkstra():
    d = [[INF] * K for _ in range(N)]
    d[0][0] = 0
    q = [(0, 0)]
    while q:
        w, c = heapq.heappop(q)
        for nxt, wei in city[c]:
            # ** 포인트 **
            # d 에 데이터를 추가한 후, sort 함으로써
            # k 개의 길이가 추가되지 않았다면 마지막은 항상 INF
            # 마지막 값에 최소 길이를 계속
            if d[nxt][-1] > wei + w:
                d[nxt][-1] = wei + w
                d[nxt].sort()
                heapq.heappush(q, (wei + w, nxt))
    return d

N, M, K = map(int, input().split())
city = [[]for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    city[a-1].append((b-1, c))
for l in dijkstra():
    print(l[-1] if l[-1] < INF else -1)