# 한 개의 회의실이 있다
# 이를 사용하고자 하는 N개의 회의 사용 표를 만들고자 한다
# 각 회의의 시작, 끝 시간이 주어져있고, 다른 회의와 중복 불가능 하다
# 회의실을 사용할 수 있는 회의의 최대 개수를 구하라
# * 회의의 종료와 시작은 동시에 일어날 수 있다
# * 회의 시작 시간과 종료 시간이 같다면 시작하자마자 끝나는 경우로 생각한다

import sys
input = sys.stdin.readline

N = int(input())
timetable = [[*map(int, input().split())]for _ in range(N)]
# ** 끝 시간에 대해서 정렬 하고, 동일하다면 시작 시간에 대해서 정렬 필요
timetable.sort(key=lambda x: (x[1], x[0]))
cnt = now = 0
for s, e in timetable:
    if s >= now:
        cnt+=1
        now = e
print(cnt)
