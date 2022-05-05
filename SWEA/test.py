for k in range(100):
    n = 1
    for i in range(31, -1, -1):
        n *= n
        if k & (1<<i):
            n *= 2
    print(n)

def perm(lst, n):
    ret = []
    if n > len(lst):
        return ret
    if n == 1:
        for i in lst:
            ret.append([i])
    elif n > 1:
        for i in range(len(lst)):
            tmp = [i for i in lst]
            tmp.remove(list[i])
            for p in perm(tmp, n-1):
                ret.append([lst[i]] + p)
    return ret

def comb(lst, n):
    ret = []
    if n > len(lst):
        return ret
    if n == 1:
        for i in lst:
            ret.append([i])
    elif n > 1:
        for i in range(len(lst) - n + 1):
            for c in comb(lst[i+1:], n-1):
                ret.append([lst[i]] + c)
    return ret
