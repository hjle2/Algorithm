def cal(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b


def calall(q):
    ans = q[0]
    for i in range(1, len(q), 2):
        ans = cal(ans, q[i], q[i + 1])
    return ans


def make_br(n, m_n, q, s):
    if n == m_n - 1:
        return calall(q + [s[n]])
    if n == m_n - 3:
        br = q + [cal(s[n], s[n + 1], s[n + 2])]
        no_br = q + [s[n], s[n + 1]]
        return max(make_br(n + 2, m_n, no_br, s), calall(br))
    br = q + [cal(s[n], s[n + 1], s[n + 2]), s[n + 3]]
    no_br = q + [s[n], s[n + 1]]
    return max(make_br(n + 2, m_n, no_br, s), make_br(n + 4, m_n, br, s))


def sol(n, s):
    s = list(int(i) if i not in ['+','-','*'] else i for i in s)
    return make_br(0, n, [], s)


print(sol(int(input()), input()))
