import heapq

n = int(input())
task = []
max_day = 0
for _ in range(n):
    d, w = map(int, input().split())
    task.append((d, w))
    max_day = max(max_day, d)
task.sort(key=lambda x: (-x[0], -x[1]))

ans, idx = 0, 0
que = []
while True:
    while idx < n and max_day <= task[idx][0]:
        heapq.heappush(que, -task[idx][1])
        idx += 1
    max_day -= 1
    if max_day < 0:
        break
    if que:
        ans -= heapq.heappop(que)
print(ans)