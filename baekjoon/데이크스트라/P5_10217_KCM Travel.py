import heapq
import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

def main():
    N, M, K = map(int, input().split())
    edge = [[] for _ in range(N)]
    dp = [[INF] * (M + 1) for _ in range(N)]

    for _ in range(K):
        u, v, c, d = map(int, input().split())
        edge[u-1].append((v-1, c, d))

    dp[0][0] = 0

    que = deque([(0, 0, 0)])  # Time Cost Node
    # que = [(0, 0, 0)]
    while que:
        time, cost, node = que.popleft()
        # time, cost, node = heapq.heappop(que)

        if dp[node][cost] < time:
            continue

        for nxt, c, t, in edge[node]:
            C, T = cost + c, time + t

            if C > M or T >= dp[nxt][C]: continue
            for i in range(C, M + 1):
                if T < dp[nxt][i]:
                    dp[nxt][i] = T
                else: break
            que.append((T, C, nxt))
            # heapq.heappush(que, (T, C, nxt))

    ans = min(dp[N-1])
    print(ans if ans != INF else 'Poor KCM')

for _ in range(int(input())):
    main()