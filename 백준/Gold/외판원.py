def TSP(cur, v):
    # 모든 노드를 방문
    if v == END:
        # 현재 노드에서 0번으로 가는 경로가 있으면,
        if graph[cur][0]:
            return graph[cur][0] # 최소비용 반환
        else:
            return 1e9

    # 이미 상태를 계산한 값이 있다면, 그대로 사용
    if dp[cur][v] != 1e9: return dp[cur][v]

    for i in range(n):
        # 현재 노드에서 i노드로 가는 길이 없으면 패스
        if graph[cur][i] == 0: continue
        # 이미 방문한 노드면 패스
        if v & (1 << i): continue

        # i번 노드 방문 처리 후 최소 비용 반환
        tmp = TSP(i, v | 1 << i)
        dp[cur][v] = min(dp[cur][v], graph[cur][i], + tmp)

    return dp[cur][v]


n = int(input())
END = (1 << n) -1
graph = [[*map(int, input().split())]for _ in range(n)]

dp = [[1e9] * (1 << n) for _ in range(n)]
print(TSP(0, 1))
