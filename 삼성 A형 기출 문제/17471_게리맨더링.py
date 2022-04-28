def isconnected(lst):
    if not lst or len(lst) == N: return False
    selected = [i not in lst for i in range(N)]
    q = [lst[0]]
    selected[lst[0]] = True
    while q:
        n = q.pop(0)
        for c in conn[n]:
            if c-1 in lst and not selected[c-1]:
                q.append(c-1)
                selected[c-1] = True
    return all(selected)

def make_case(n, q):
    global ans
    if q and isconnected(q):
        p = [i for i in range(N) if i not in q]
        if isconnected(p):
            diff = 0
            for i in range(N):
                diff += people[i] if i in q else -people[i]
            ans = min(ans, abs(diff))

    for i in range(n, N):
        make_case(i+1, q + [i])

N = int(input())
people = list(map(int, input().split()))
conn = [list(map(int, input().split()))[1:]for _ in range(N)]
ans = 999999
make_case(0, [])
print(ans if ans < 999999 else -1)
