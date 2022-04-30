# palindromic
import itertools


def palin(perm):
    ret = 0
    for p in perm:
        p = [i for i in p]
        i = 0
        while p and p[i] == '0':
            p.pop(0)
        if not p: continue
        a = int(''.join(p))
        p.reverse()
        b = int(''.join(p))
        if a == b:
            ret = max(ret, a)
    return ret


def solution(S):
    s = list(S)
    ans = int(max(s))
    for n in range(2, len(s)):
        perm = itertools.permutations(s, n)
        ans = max(ans, palin(perm))
    return str(ans)

