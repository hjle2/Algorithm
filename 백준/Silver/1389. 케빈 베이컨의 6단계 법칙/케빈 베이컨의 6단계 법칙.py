from collections import deque


def get_step(a, b):
    ret = 0
    que = deque([(a, 0)])
    v = [False] * (n+1)
    v[a] = True
    while que:
        cur, cnt = que.popleft()
        if cur == b:
             return cnt
        for nxt in graph[cur]:
            if v[nxt]: continue
            que.append((nxt, cnt+1))
            v[nxt] = True
    return ret


def get_step_sum(a):
    ret = 0
    for i in range(1, n+1):
        if i == a: continue
        ret += get_step(a, i)
    return ret


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bacon_n = 1e9
ans = 0
for i in range(1, n+1):
    sum_step = get_step_sum(i)
    if sum_step < bacon_n:
        ans = i
        bacon_n = sum_step
print(ans)