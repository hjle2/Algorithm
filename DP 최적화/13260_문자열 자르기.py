# # Knuth Optimization
# # 크누스 최적화
# # M 회 자르는 것 이 아니라
# # M+1 개의 문자열을 합친다. 라고 생각하면
# # 백준 11066 번의 문제와 동일하다
# # DP 로 해결 가능
# import sys
#
# sys.setrecursionlimit(10**6)
# def solve(s, e):
#     if s == e:
#         return 0
#     if DP[e][s]:
#         return DP[e][s]
#     if s+1 == e:
#         DP[e][s] = lst[s] + lst[e]
#         return DP[e][s]
#
#     ret = min(solve(s+1, e), solve(s, e-1))
#     for i in range(s+1, e-s-1):
#         ret = min(ret, solve(s, i) + solve(i+1, e))
#     DP[e][s] = ret + sum(lst[s:e+1])
#     return DP[e][s]
#
#
# N, M = map(int, input().split())
# p = 0
# lst = []
# for n in sorted(map(int, input().split())):
#     lst.append(n-p)
#     p = n
# lst.append(N-p)
#
# # M 회 자른다면 문자열은 M+1 개가 되기 떄문에 DP 는 M+1로 설정
# DP = [[0]*i for i in range(M+1)]
#
# print(solve(0, M))


# 메모리 초과 문제로 재귀함수 대신 반복문으로 풀어서 해결

INF = 10**18
N, M = map(int, input().split())
lst = [0] + sorted(map(int, input().split())) + [N]
M += 1
dp = [[INF]*M for _ in range(M)]
for i in range(M):
    dp[i][i] = 0

for d in range(1, M):
    for s in range(M - d):
        e = s + d
        for i in range(s, e+1):
            if i < M-1 and dp[s][e] > dp[s][i] + dp[i+1][e]:
                dp[s][e] = dp[s][i] + dp[i+1][e]
        dp[s][e] += lst[e+1] - lst[s]
print(dp[0][-1])
