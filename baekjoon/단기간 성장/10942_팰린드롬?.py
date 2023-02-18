import sys

input = sys.stdin.readline

def bellman_ford():
    dist[1] = 0
    for i in range(N):
        for a, b, c in busLine:
            if dist[a] != INF and dist[b] > dist[a] + c:
                if i == N-1:
                    return True
                dist[b] = dist[a] + c
    return False

INF = 1e9
N, M = map(int, input().split())
busLine = []
for _ in range(M):
    busLine.append([*map(int, input().split())])
dist = [INF] * (N+1)
if bellman_ford():
    print(-1)
else:
    for i in range(2, N+1):
        print(dist[i] if dist[i] < INF else -1)
