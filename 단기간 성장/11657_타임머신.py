import sys
input = sys.stdin.readline

def isPossibleToPast(now, t, first):
    if not first and now == 1:
        if t < 0:
            print(-1)
            exit()
        return
    for dest, time in busLines[now]:
        isPossibleToPast(dest, t + time, False)

N, M = map(int, input().split())
busLines = [[]for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    busLines[a].append((b, c))
isPossibleToPast(1, 0, True)