from copy import deepcopy

N = 11
max_scoredif = 0
ans = [-1]

def scorediff(peach, me):
    ans = 0
    for i in range(N):
        if peach[i] == 0 and me[i] == 0: continue
        if peach[i]>=me[i]:
            ans -= N-1-i
        else:
            ans += N-1-i
    return ans

def comparesmaller(me):
    global ans
    for i in range(N-1, -1, -1):
        if ans[i] < me[i]:
            ans = deepcopy(me)
            return
        elif ans[i] > me[i]:
            return


def dfs(n, i, peach, me):
    global max_scoredif
    global ans
    tag = True
    if n == 0:
        n_scoredif = scorediff(peach, me)
        if n_scoredif > max_scoredif:
            max_scoredif = n_scoredif
            ans = deepcopy(me)
        elif n_scoredif>0 and n_scoredif == max_scoredif:
            comparesmaller(me)
        return
    for idx in range(i, N):
        if peach[idx] + 1 <= n:
            tag = False
            me[idx] = peach[idx]+1
            dfs(n - peach[idx]-1, idx + 1, peach, me)
            me[idx] = 0
    if tag:
        me[-1] += n
        dfs(0, N, peach, me)
        me[-1] -= n
        return

def solution(n, info):
    global ans
    dfs(n, 0, info, [0]*N)
    return ans
solution(5,[2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])