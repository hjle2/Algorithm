def ispossible(n):
    for i in range(n):
        if ar[i] == ar[n] or abs(ar[n]-ar[i]) == abs(n-i):
            return False
    return True


def dfs(n):
    global cnt
    if n == N:
        cnt += 1
        return

    for i in range(N):
        ar[n] = i
        if ispossible(n):
            dfs(n+1)

cnt = 0
N = int(input())
ar = [0] * N
dfs(0)
print(cnt)
