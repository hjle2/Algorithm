import heapq
import sys
input = sys.stdin.readline

n = int(input())
conference = []
for _ in range(n):
    a, b, c = map(int, input().split())
    conference.append((b, c))
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