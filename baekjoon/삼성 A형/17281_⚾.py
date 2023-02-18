def make_case(n, lst):
    ret = []
    if n == 1:
        for i in lst:
            ret.append([i])
    elif n>1:
        for i in range(len(lst)):
            tmp = [i for i in lst]
            tmp.remove(lst[i])
            for p in make_case(n-1, tmp):
                ret.append([lst[i]] + p)
    return ret

def play(i_n, i, lst):
    cnt = 0
    r1 = r2 = r3 = 0
    score = 0
    while cnt < 3:
        p = a[i_n][lst[i]]
        if p == 0:
            cnt += 1
        elif p == 1:
            score += r3
            r1, r2, r3 = 1, r1, r2
        elif p == 2:
            score += r2 + r3
            r1, r2, r3 = 0, 1, r1
        elif p == 3:
            score += r1 + r2 + r3
            r1, r2, r3 = 0, 0, 1
        elif p == 4:
            score += 1 + r1 + r2 + r3
            r1, r2, r3 = 0, 0, 0
        i = (i+1)%9
    return i, score

n = int(input())
a = [list(map(int, input().split()))for _ in range(n)]
ans = 0
for p in make_case(8, range(1, 9)):
    p.insert(3, 0)
    i = score = 0
    for i_n in range(n):
        i, s = play(i_n, i, p)
        score += s
    ans = max(ans, score)
print(ans)