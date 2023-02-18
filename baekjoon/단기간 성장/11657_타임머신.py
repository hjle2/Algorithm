import sys

input = sys.stdin.readline


def bellman_ford():
    for i in range(N):
        for now, nxt, t in busLines:
            if ans[now] != INF and ans[nxt] > ans[now] + t:
                if i == N-1:
                    return True
                ans[nxt] = ans[now] + t
    return False

INF = 1e9
N, M = map(int, input().split())
busLines = []
for _ in range(M):
    a, b, c = map(int, input().split())
    busLines.append((a, b, c))

ans = [INF] * (N + 1)
ans[1] = 0
if bellman_ford():
    print(-1)
else:
    for i in ans[2:]:
        print(i if i < INF else -1)
