import heapq

def solve(k, file):
    heapq.heapify(file)

    ret = 0
    while len(file) > 1:
        tmp = heapq.heappop(file) + heapq.heappop(file)
        ret += tmp
        heapq.heappush(file, tmp)
    return ret


for _ in range(int(input())):
    k = int(input())
    file = [*map(int, input().split())]
    print(solve(k, file))
