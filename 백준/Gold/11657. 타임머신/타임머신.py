n, m = map(int, input().split())
graph = [[*map(int, input().split())]for _ in range(m)]


def bellmanford(s):
    d = [1e9] * (n+1)
    d[s] = 0

    for i in range(n):                                  # 모든 노드 수 만큼
        for j in range(m):                              # 모든 경로에 매번 검사
            cur, nxt, wei = graph[j]
            if d[cur] != 1e9 and d[nxt] > d[cur] + wei: # 현재 간선을 거쳐 이동하는 거리가 더 짧은 경우
                d[nxt] = d[cur] + wei                   # 거리를 갱신해준다
                if i == n-1:                            # 음수 순환 존재
                    return False
    return d

d = bellmanford(1)
if not d:
    print(-1)
else:
    for i in range(2, n+1):
        print(d[i] if d[i] < 1e9 else -1)
