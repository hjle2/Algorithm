N, M, K = map(int, input().split())
board = [[*map(int, input().split())]for _ in range(N)]
people = []
for _ in range(M):
    a, b = map(int, input().split())
    people.append((a-1, b-1))
