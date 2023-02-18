N = int(input())
A = [[*map(int, input().split())]for _ in range(N)]


def clone(ar):
    a = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            a[r][c] = ar[r][c]
    return a


def push(d, ar):
    if d < 2:   # 좌우
        for r in range(N):
            flag, temp = False, []
            for c in [range(N), range(N-1, -1, -1) ][d%2]: # 좌, 우로 밀때
                if not ar[r][c]: continue
                if not temp or temp[-1] != ar[r][c] or flag:
                    temp.append(ar[r][c])
                    flag = False
                else:
                    temp[-1] *= 2
                    flag = True
            if d == 0:  # 좌
                temp = temp + [0] * (N - len(temp))
            else:       # 우
                temp = [0] * (N - len(temp)) + temp[::-1]
            ar[r] = temp
    else:       # 상하
        for c in range(N):
            flag, temp = False, []
            for r in [range(N), range(N-1, -1, -1) ][d%2]: # 상, 하로 밀때
                if not ar[r][c]: continue
                if not temp or temp[-1] != ar[r][c] or flag:
                    temp.append(ar[r][c])
                    flag = False
                else:
                    temp[-1] *= 2
                    flag = True
            if not d%2:  # 상
                temp = temp + [0] * (N - len(temp))
            else:       # 하
                temp = [0] * (N - len(temp)) + temp[::-1]
            for r in range(N):
                ar[r][c] = temp[r]


def dfs(cnt, ar):
    if cnt == 0:
        return max(max(ar[i])for i in range(N))

    ret = max(max(ar[i])for i in range(N))
    for d in range(4):
        tmp = clone(ar)
        push(d, tmp)
        ret = max(ret, dfs(cnt-1, tmp))
    return ret


print(dfs(5, A))
