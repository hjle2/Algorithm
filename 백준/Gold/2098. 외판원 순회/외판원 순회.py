n = int(input())
graph = [[*map(int, input().split())]for _ in range(n)]
# 현재 노드 i, 이전에 방문한 노드의 집합 j (bitmasking)
dp = [[0] * (1 << n) for _ in range(n)]

# 현재노드 cur, 방문한 노드들의 집합 visited의 최소 비용 계산하기
def dfs(cur, visited):
    # 모든 노드를 방문했다면, 재귀 그만!
    if visited == (1 << n) - 1:
        # 0으로 돌아가는 길이 있다면 0으로 돌아가는 최솟값 반환
        # 0으로 돌아가는 길이 없다면 유효하지 않은 경로이므로 최댓값 반환
        return graph[cur][0] or 1e9
    
    # 이미 계산한 노드라면 계산되어 있는 최솟값 반환
    if dp[cur][visited]:
        return dp[cur][visited]

    dp[cur][visited] = 1e9
    for i in range(n):
        # 방문하지 않은 노드에 대해서 길이 있다면, 최솟값을 구한다
        if visited & (1 << i) or not graph[cur][i]: continue
        dp[cur][visited] = min(dp[cur][visited], dfs(i, visited | (1 << i)) + graph[cur][i])
    return dp[cur][visited]

print(dfs(0, 1 << 0))
