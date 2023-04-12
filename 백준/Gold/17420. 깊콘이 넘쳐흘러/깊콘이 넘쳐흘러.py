n = int(input())
left = [*map(int, input().split())]
plan = [*map(int, input().split())]

day = [[]for _ in range(n)]
for i in range(n):
    day[i] = [left[i], plan[i]]
day.sort(key=lambda x:(x[1], x[0]))


def get_cnt(left_day, plan_day):
    if left_day >= plan_day:
        return 0
    else:
        sub = plan_day - left_day + 29
        cnt = sub // 30
        return cnt

cnt = 0
prv_max = day[0][1]
cur_max = -1

for i in range(n):
    left_day, plan_day = day[i]

    if left_day < prv_max:
        if prv_max < plan_day:
            prv_max = plan_day

        tmp_cnt = get_cnt(left_day, prv_max)
        left_day += tmp_cnt * 30
        cnt += tmp_cnt

    cur_max = max(cur_max, left_day)

    if i + 1 < n and day[i][1] != day[i+1][1]:
        prv_max = cur_max

print(cnt)