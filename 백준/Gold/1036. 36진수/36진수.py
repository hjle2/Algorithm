def to_num(chr):
    ret = 0
    for i in range(len(chr)):
        c = chr[-1-i]
        if c <= '9':
            c = int(c)
        else:
            c = ord(c) - A
        if is_Z[c]:
            c = 35
        ret += 36 ** i * c
    return ret


def to_chr(num):
    ret = ''
    v = 0
    if not num:
        return 0
    while num:
        tmp = num % 36
        if tmp > 9:
            ret = chr(tmp + A) + ret
        else:
            ret = str(tmp) + ret
        num //= 36
        v += 1
    return ret


def count(chr):
    for i in range(len(chr)):
        c = chr[-1-i]
        if c <= '9':
            c = int(c)
        else:
            c = ord(c) - A
        cnt[c] += 36 ** i * (35 - c)


n = int(input())
nums = [[*input()] for _ in range(n)]
k = int(input())
A = ord('A') - 10

cnt = [0] * 36
for num in nums:
    count(num)

is_Z = [False] * 36
for _ in range(k):
    max_v = max(cnt[:-1])
    max_i = cnt.index(max_v)
    is_Z[max_i] = True
    cnt[max_i] = 0

ans = 0
for num in nums:
    ans += to_num(num)
print(to_chr(ans))
