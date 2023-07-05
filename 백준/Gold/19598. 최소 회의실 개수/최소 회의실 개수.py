import heapq
import sys
input = sys.stdin.readline

n = int(input())
conference = [[*map(int, input().split())]for _ in range(n)]
conference.sort()

que = []
for s, e in conference:
    if not que:
        heapq.heappush(que, e)
    else:
        end = heapq.heappop(que)
        if end <= s:
            heapq.heappush(que, e)
        else:
            heapq.heappush(que, e)
            heapq.heappush(que, end)
print(len(que))