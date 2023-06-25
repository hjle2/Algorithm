n = int(input())
string = [*input()]
a = ord('a')

alpha_ar = [0] * 26
alpha_cnt = 0

s, e = 0, 0
ans = 0

while s < len(string) and e < len(string):
    if alpha_cnt <= n:
        if alpha_ar[ord(string[e]) - a] == 0:
            alpha_cnt += 1
        alpha_ar[ord(string[e]) - a] += 1
        ans = max(ans, e - s)
        e += 1
    else:
        if alpha_ar[ord(string[s]) - a] == 1:
            alpha_cnt -= 1
        alpha_ar[ord(string[s]) - a] -= 1
        s += 1
if alpha_cnt <= n:
    ans = max(ans, e-s)
print(ans)