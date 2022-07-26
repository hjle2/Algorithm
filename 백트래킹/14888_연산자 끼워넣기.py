def operate(a, op, b):
    if op == 0:
        return a+b
    elif op == 1:
        return a-b
    elif op == 2:
        return a*b
    else:
        if a >= 0:
            return a//b
        else:
            return (-a)//b * -1


def dfs(n, s):
    global minA, maxA
    if n == N:
        minA = min(minA, s)
        maxA = max(maxA, s)
        return
    for i in range(4):
        if op[i]:
            op[i] -= 1
            dfs(n+1, operate(s, i, A[n]))
            op[i] += 1


N = int(input())
A = [*map(int, input().split())]
op = [*map(int, input().split())]
minA, maxA = 1e9, -1e9
dfs(1, A[0])
print(maxA, minA, sep='\n')

# 연산을 eval 함수를 이용하면 C++14 기준으로 되나봄.. 통과됨..