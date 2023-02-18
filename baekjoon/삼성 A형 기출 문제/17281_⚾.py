def play(i_n, i_i, q):
    r1 = r2 = r3 = cnt = score = 0
    while cnt < 3:
        v = A[i_n][q[i_i]]
        if v == 1:
            score += r3
            r1, r2, r3 = 1, r1, r2
        elif v == 2:
            score += r2 + r3
            r1, r2, r3 = 0, 1, r1
        elif v == 3:
            score += r1 + r2 + r3
            r1, r2, r3 = 0, 0, 1
        elif v == 4:
            score += 1 + r1 + r2 + r3
            r1 = r2 = r3 = 0
        elif v == 0:
            cnt += 1
        i_i = (i_i + 1)%9
    return i_i, score


def make_case(q, n):
    global ret
    if 8 == n:
        q.insert(3, 0)
        i_i = ans = 0
        for i_n in range(N):
            i_i, score = play(i_n, i_i, q)
            ans += score
        ret = max(ret, ans)
    else:
        for i in range(1, 9):
            if i not in q:
                make_case(q+[i], n+1)


N = int(input())
A = [list(map(int, input().split()))for _ in range(N)]
ret = 0
make_case([], 0)
print(ret)