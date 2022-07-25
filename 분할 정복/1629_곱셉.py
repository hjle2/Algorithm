# def dfs(n):
#     if n == 1:
#         return A % C
#     if n == 2:
#         return A * A % C
#     m = n//2
#     t = dfs(m)
#     t *= t
#     if n%2:
#         t *= A
#     return t % C
#
# A, B, C = map(int, input().split())
# print(dfs(B))
print(pow(*map(int,input().split())))
