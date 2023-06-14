import heapq

n = int(input())
cards = [int(input()) for _ in range(n)]
heapq.heapify(cards)

ans = 0
while len(cards) > 1:
    tmp = heapq.heappop(cards) + heapq.heappop(cards)
    ans += tmp
    heapq.heappush(cards, tmp)
print(ans)