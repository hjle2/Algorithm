from collections import deque


def solve(importane):
     que = deque([i for i in range(n)])

     turn = 1

     while que:
         cur = que.popleft()
         if not que or max(importane) <= importane[cur]:
             if cur == m:
                 return turn
             else:
                 importane[cur] = 0
                 turn += 1
         else:
             que.append(cur)


for _ in range(int(input())):
    n, m = map(int, input().split()) # 문서의 개수, 궁금한 문서의 현재 위치
    importance = [*map(int, input().split())]
    print(solve(importance))
