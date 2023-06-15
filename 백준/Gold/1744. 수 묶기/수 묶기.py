n = int(input())
negative = []
positive = []
zero = False
for i in range(n):
    x = int(input())
    if x == 0:
        zero = True
    elif x < 0:
        negative.append(x)
    else:
        positive.append(x)

negative.sort()
positive.sort(reverse=True)
# -는 -끼리 묶어서 상쇄시키자
# +는 큰수끼리 곱해서 더 크게 만들자
# 0이 있다면 하나 남은 음수는 0으로 처리
# 0이 없으면 하나 남은 음수는 그냥 더해주기
ans = 0
for i in range(0, len(negative) - 1, 2):
    ans += negative[i] * negative[i+1]
if len(negative) % 2 != 0 and not zero:
    ans += negative[-1]
for i in range(0, len(positive) - 1, 2):
    tmp = positive[i] * positive[i+1]
    if positive[i] + positive[i+1] <= tmp:
        ans += tmp
    else:
        ans += positive[i] + positive[i+1]
if len(positive) % 2 != 0:
    ans += positive[-1]
print(ans)