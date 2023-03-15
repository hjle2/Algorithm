n = int(input())
num = sorted([int(input())for _ in range(n)])
ans = 0

# 양수 (1보다 큰 수) 는 큰 순서대로 곱한다
# 음수가 있으면, 음수끼리는 곱해야 한다
# 음수와 0이 있으면 곱한다
# 그 외 음수는 그냥 더해준다

while num and num[0] <= 0:
    n = num.pop(0)
    if num and num[0] <= 0:
        m = num.pop(0)
        n *= m
    ans += n
while num and num[-1] > 0:
    n = num.pop()
    if num:
        m = num.pop()
        if m > 1:
            n *= m
        else:
            n += m
    ans += n
print(ans)



