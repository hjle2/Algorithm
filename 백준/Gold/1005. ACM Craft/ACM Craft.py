def makeTurn():
    turn = []
    for i in range(1, N+1):
        if not cnt[i]:
            turn.append(i)
    ord = []
    while turn:
        x = turn.pop(0)
        ord.append(x)
        if not edge[x]: continue
        for j in edge[x]:
            cnt[j] -= 1
            if cnt[j] == 0:
                turn.append(j)
    return ord


def solve():
    for i in turn:
        if not link[i]: continue
        v = 0
        for j in link[i]:
            v = max(v, hour[j])
        hour[i] += v
    print(hour[W])


for _ in range(int(input())):
    N, K = map(int, input().split())
    hour = [0, *map(int, input().split())]
    cnt = [0] * (N+1)
    edge = [[]for _ in range(N+1)]
    link = [[] for _ in range(N+1)]
    for _ in range(K):
        a, b = map(int, input().split())
        edge[a].append(b)
        link[b].append(a)
        cnt[b] += 1
    W = int(input())
    turn = makeTurn()
    solve()