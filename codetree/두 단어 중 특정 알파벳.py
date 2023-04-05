n = int(input())
lower_a = ord('a')


def count(word, cnt):
    for w in [*word]:
        idx = ord(w) - lower_a
        cnt[idx] += 1

ans = [0] * 26
for i in range(n):
    a, b = input().split()
    ar_a = [0] * 26
    ar_b = [0] * 26
    count(a, ar_a)
    count(b, ar_b)

    for i in range(26):
        tmp = max(ar_a[i], ar_b[i])
        if tmp:
            ans[i] += tmp


print(*ans, sep='\n')
