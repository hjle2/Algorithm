s, p = map(int, input().split())
string = input()
ACGT = [*map(int, input().split())]

ans = 0
acgt_cnt = [0] * 4

for j in range(p-1):
    if string[j] == 'A':
        acgt_cnt[0] += 1
    elif string[j] == 'C':
        acgt_cnt[1] += 1
    elif string[j] == 'G':
        acgt_cnt[2] += 1
    else:
        acgt_cnt[3] += 1

for i in range(s-p+1):

    if string[i+p-1] == 'A':
        acgt_cnt[0] += 1
    elif string[i+p-1] == 'C':
        acgt_cnt[1] += 1
    elif string[i+p-1] == 'G':
        acgt_cnt[2] += 1
    else:
        acgt_cnt[3] += 1

    flag = True
    for j in range(4):
        if acgt_cnt[j] < ACGT[j]:
            flag = False
            break
    if flag:
        # ans.append(str(string[i:i+p]))
        ans += 1

    if string[i] == 'A':
        acgt_cnt[0] -= 1
    elif string[i] == 'C':
        acgt_cnt[1] -= 1
    elif string[i] == 'G':
        acgt_cnt[2] -= 1
    else:
        acgt_cnt[3] -= 1
print(ans)