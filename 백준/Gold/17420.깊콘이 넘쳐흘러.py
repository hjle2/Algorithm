n = int(input())
left = [*map(int, input().split())]
plan = [*map(int, input().split())]

day = [[]for _ in range(n)]
for i in range(n):
    day[i] = [plan[i], left[i]]
day.sort(key=lambda x:(x[0], x[1]))


def get_cnt(left_day, plan_day):
    if left_day >= plan_day:
        return 0
    else:
        sub = plan_day - left_day + 29
        cnt = sub // 30
        return cnt


def get_index():
    first_plan = day[0][0]
    min_left = 1e9
    min_idx = 0
    for i, (plan_day, left_day) in enumerate(day):
        if plan_day != first_plan:
            return min_idx

        if left_day < plan_day:
            tmp_cnt = get_cnt(left_day, plan_day)
            left_day += tmp_cnt * 30

        if left_day < prv_max:
            tmp_cnt = get_cnt(left_day, prv_max)
            left_day += tmp_cnt * 30

        if min_left > left_day:
            min_idx = i
            min_left = left_day
    return min_idx

cnt = 0
prv_max = 0

while day:
    i = get_index()
    plan_day, left_day = day.pop(i)

    if left_day < prv_max:
        tmp_cnt = get_cnt(left_day, prv_max)
        left_day += tmp_cnt * 30
        cnt += tmp_cnt

    if left_day > plan_day:
        prv_max = left_day
        continue

    tmp_cnt = get_cnt(left_day, plan_day)
    left_day += tmp_cnt * 30
    cnt += tmp_cnt

    prv_max = left_day

print(cnt)
# 5
# 10 20 30 40 50
# 50 40 30 20 10
# 40점 짜리 답..ㅎ
