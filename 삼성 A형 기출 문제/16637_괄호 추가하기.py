def cal(a, op, b):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b


def calall(inp):
    ans = inp[0]
    for i in range(1, len(inp), 2):
        ans = cal(ans, inp[i], inp[i+1])
    return ans


def make_br(n, q):
    if n == N-1:
        return calall(q + [inp[n]])

    if n == N-3:
        no_br = q + [inp[n], inp[n+1]]
        br = q + [cal(inp[n], inp[n+1], inp[n+2])]
        return max(calall(br), make_br(n+2, no_br))

    br = q + [cal(inp[n], inp[n+1], inp[n+2]), inp[n+3]]
    no_br = q + [inp[n], inp[n+1]]
    return max(make_br(n+2, no_br), make_br(n+4, br))


N = int(input())
inp = list(int(i) if i not in ['+','-','*'] else i for i in input())

print(make_br(0, []))