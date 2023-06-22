import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input()) * 10 ** 7
        n = int(input())
        rego = [int(input())for _ in range(n)]
        rego.sort()
        s, e = 0, n-1
        flag = True
        while s < e:
            tmp = rego[s] + rego[e]
            if tmp == x:
                flag = False
                print('yes', rego[s], rego[e])
                break
            elif tmp < x:
                s += 1
            else:
                e -= 1
        if flag:
            print('danger')
    except:
        break
