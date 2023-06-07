import sys

input = sys.stdin.readline
n = int(input())
cities = [list(map(int, input().split())) for _ in range(n)]
# (1 << N) - 1 ==> 'N개의 비트를 모두 켠다'와 같음
VISITED_ALL = (1 << n) - 1

cache = [[None] * (1 << n) for _ in range(n)]
INF = float('inf')
idx = 1


def find_path(last, visited):
    if visited == VISITED_ALL:
   

        return cities[last][0] or INF  # 마지막 도착 도시에서 출발 도시인 0으로 가야됨.(문제 조건)

    if cache[last][visited] is not None:
        return cache[last][visited]

    tmp = INF
    for city in range(n):
        if visited & (1 << city) == 0 and cities[last][city] != 0:
            tmp = min(tmp, find_path(city, visited | (1 << city)) + cities[last][city])
    cache[last][visited] = tmp
    return tmp


print(find_path(0, 1 << 0))