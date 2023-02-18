# 가장 많은 돈을 벌 수 있도록 순회강연 하는 방법으 ㄹ구하라
# 하루에 최대 한 곳

import heapq
# n = int(input())
#
# listDByP = [[]for _ in range(10000)]
#
# for _ in range(n):
#     d, p = map(int, input().split())
#     heapq.heappush(listDByP[p-1], -d)
#
# ans, cnt = 0, 0
# for i in range(9999, -1, -1):
#     max_ans, idx = 0, -1
#     for j in range(i, 10000):
#         if not listDByP[j]: continue
#         max_cur = -listDByP[j][0]
#         if max_cur > max_ans:
#             max_ans = max_cur
#             idx = j
#     if idx >= 0:
#         heapq.heappop(listDByP[idx])
#         ans += max_ans
# print(ans)

n = int(input())
lec = [[*map(int, input().split())]for _ in range(n)]
q = []
for w, d in sorted(lec, key=lambda x:x[1]):
    heapq.heappush(q, w)
    if d < len(q): heapq.heappop(q)
print(sum(q))