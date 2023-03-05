import sys
import heapq
si = sys.stdin.readline

n = int(si())
day_cup = sorted([[*map(int, input().split())]for _ in range(n)])

que = []

for day, cup in day_cup:
    heapq.heappush(que, cup)

    # 지금까지 푼 문제의 수가 현재 날짜보다 클 수 없기 때문에 pop으로 적은 컵라면 순으로 제거해준다
    while len(que) > day:
        heapq.heappop(que)
print(sum(que))
