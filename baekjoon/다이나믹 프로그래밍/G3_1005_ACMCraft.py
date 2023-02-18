# # 건물의 갯수 2 <= N <= 1000
# # 건설 순서 규칙의 개수 1 <= K <= 100,000
# # 각 건물을 건설하는 데 걸리는 시간
# # A 건물을 지어야 B 건물이 가능한 순서 쌍
#
#
# # 위상 정렬
# # 진입 차수가 0인 정점을 큐에 삽입
# # 큐에서 정점을 꺼내고, 정점이 가리키는 간선을 모두 삭제
# # 위의 상태에서 진입 차수가 0인 정점을 큐에 삽입
# from copy import deepcopy
#
#
# def solve():
#     turn = []
#     for i in range(1, N+1):
#         if not cnt[i]:
#             turn.append(i)
#     while turn:
#         x = turn.pop(0)
#         if not edge[x]: continue
#         for j in edge[x]:
#             cnt[j] -= 1
#             hour[j] = max(hour[j], hour[x] + w[j])
#             if cnt[j] == 0:
#                 turn.append(j)
#     print(hour[W])
#
#
# # def solve():
# #     for i in turn:
# #         if not link[i]: continue
# #         v = 0
# #         for j in link[i]:
# #             v = max(v, hour[j])
# #         hour[i] += v
# #     print(hour[W])
#
#
# for _ in range(int(input())):
#     N, K = map(int, input().split())
#     hour = [0, *map(int, input().split())]
#     w = deepcopy(hour)
#     cnt = [0] * (N+1)
#     edge = [[]for _ in range(N+1)]
#     for _ in range(K):
#         a, b = map(int, input().split())
#         edge[a].append(b)
#         cnt[b] += 1
#     W = int(input())
#     solve()


import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solve(w):
    if dp[w] >= 0:
        return dp[w]
    dp[w] = D[w]
    if link[w]:
        dp[w] += max(solve(x) for x in link[w])
    return dp[w]

for _ in range(int(input())):
    N, K = map(int, input().split())
    D = [0, *map(int, input().split())]
    link = defaultdict(list)
    for _ in range(K):
        a, b = map(int, input().split())
        link[b].append(a)
    W = int(input())
    dp = [-1] * (N-1)
    print(solve(W))