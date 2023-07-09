from collections import Counter


def solve():
    a = ord('A')
    flag = False
    flag_c = ''
    ans = ''
    for i in range(26):
        c = chr(a + i)
        if not counter[c]: continue
        if counter[c] % 2:
            if flag:
                return "I'm Sorry Hansoo"
            flag = True
            flag_c = c

        ans += c * (counter[c] // 2)
    ans += flag_c

    n = len(ans)
    if flag:
        n -= 1
    k = n - 1
    for i in range(n):
        ans += ans[k]
        k -= 1
    return ans


name = [*input()]
counter = Counter(name)

print(solve())