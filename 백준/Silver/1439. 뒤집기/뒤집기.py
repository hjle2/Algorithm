number = [*input().rstrip()]

cnt0, cnt1 = 0, 0
prv = -1
for num in number:
    if prv != num:
        if num == '0':
            cnt0 += 1
        if num == '1':
            cnt1 += 1
    prv = num
print(min(cnt0, cnt1))