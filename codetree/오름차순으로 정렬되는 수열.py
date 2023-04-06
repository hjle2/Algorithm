import copy
n = int(input())
num = [int(input())for _ in range(n)]
sorted_num = sorted(num)


def find_index(num):
    v = 0
    for i in range(n):
        if v <= num[i]:
            v = num[i]
        else:
            # 중간에 큰 수가 나타났을 때
            if i-2 >= 0 and num[i-2] <= num[i]:
                return i-1
            return i
    return -1


def count_same_num(sorted_num):
    v = 0
    cnt = 0
    start_index = min(wrong_index, org_index)
    end_index = max(wrong_index, org_index)
    for i in range(start_index, end_index + 1):
        if sorted_num[i] != v:
            v = sorted_num[i]
            continue
        else:
            cnt += 1
    return cnt


wrong_index = find_index(num)
wrong_v = num[wrong_index]
org_index = sorted_num.index(wrong_v)
same_num_cnt = count_same_num(sorted_num)

print(abs(wrong_index - org_index) - same_num_cnt)
