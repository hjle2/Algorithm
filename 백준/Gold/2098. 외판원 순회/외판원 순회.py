# # 현재 노드, 방문한 노드들의 집합
# def dfs(cur, visited):
#     # 현재 노드의 방문 처리
#     visited |= (1 << cur)
#
#     # 전체 노드가 모두 방문되었을 때
#     if visited == (1 << n) - 1:
#         # 0번 노드로 돌아갈 수 있는 길이 있다면
#         if graph[cur][0] != 0:
#             return graph[cur][0]
#         # 0번 노드로 돌아갈 수 있는 길이 없다면 불가능한 경로가 된다.
#         return 1e9
#
#     # 이미 방문한 적 있는 노드라면
#     if dp[visited][cur] > 0:
#         return dp[visited][cur]
#
#     # 처음 방문하는 노드일 때
#     cost = 1e9
#     for i in range(n):
#         # 현재 노드에서 갈 수 있는 노드 중에서 아직 방문하지 않은 노드일 때만
#         if graph[cur][i] != 0 and visited & (1 << i) == 0:
#             tmp = dfs(i, visited | (1 << i)) + graph[cur][i]
#             if cost > tmp:
#                 cost = tmp
#     return cost
#
#
# # 노드 수는 2 ~ 16
# n = int(input())
# graph = [[*map(int, input().split())]for _ in range(n)]
#
# # 이미 방문한 노드의 집합 i, 현재 노드 j
# dp = [[0] * n for _ in range(1 << n)]
#
# print(dfs(0, 0))

n = int(input())
INF = 1e9
graph = [[*map(int, input().split())]for _ in range(n)]
# 현재 노드 i, 이미 방문한 노드의 집합 j
dp = [[0] * (1 << n) for _ in range(n)]
ALL = (1 << n) - 1
def dfs(cur, visited):
    # 모든 노드를 방문했다면,
    if visited == ALL:
        # 0으로 돌아갈 길이 있다면, 최솟값 반환
        # if graph[cur][0] != 0:
            return graph[cur][0] or INF
        # 0으로 돌아갈 길이 없다면, 유효하지 않은 경로
        # return INF

    # 이미 방문했었던 노드라면 계산된 값 반환
    if dp[cur][visited] != 0:
        return dp[cur][visited]

    tmp = INF
    for i in range(n):
        # 길이 없거나, 이미 방문한 도시라면 패스
        if visited & (1 << i) or not graph[cur][i]: continue
        tmp = min(tmp, dfs(i, visited | (1 << i)) + graph[cur][i])
    dp[cur][visited] = tmp
    return dp[cur][visited]

print(dfs(0, 1))