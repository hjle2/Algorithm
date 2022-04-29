def getnums(ret, sep):
    for i in range(0, n-sep+1, sep):
        num = ''.join(a[i:i+sep])
        if num not in ret:
            ret.append(num)
    return ret


def sol():
    sep = n//4
    ret = getnums([], sep)
    for _ in range(sep):
        tmp = a.pop()
        a.insert(0, tmp)
        ret = getnums(ret, sep)
    ret.sort(reverse=True)
    return int(ret[k-1], 16)


for t in range(int(input())):
    n, k = map(int, input().split())
    a = list(input())
    print(f'#{t+1}', sol())
