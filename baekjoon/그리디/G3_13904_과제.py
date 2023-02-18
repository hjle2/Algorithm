# 과제마다 마감일이 있고, 과제를 끝내지 못할 수도 있다
# 하루에 한 과제를 끝낼 수 있다
# 과제를 냈을 때 얻을 수 있는 점수가 있다
# 마감일이 지난 과제는 점수를 받을 수 없다
# 받을 수 있는 가장 많은 점수를 구하라

import sys
input = sys.stdin.readline
N = int(input())
dw = sorted([[*map(int, input().split())]for _ in range(N)], key=lambda x:(-x[1], x[0]))
flag = [False] * (max(dw[i][0]for i in range(N)) + 1)
ans = 0
for d, w in dw:
    if not flag[d]:
        flag[d] = True
        ans += w
    else:
        while flag[d] and d >= 1:
            d -= 1
        if d == 0:
            continue
        else:
            flag[d] = True
            ans += w
print(ans)