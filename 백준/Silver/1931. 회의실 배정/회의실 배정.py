import sys
input = sys.stdin.readline

N = int(input())
timetable = [[*map(int, input().split())]for _ in range(N)]
timetable.sort(key=lambda x: (x[1], x[0]))
cnt = now = 0
for s, e in timetable:
    if s >= now:
        cnt+=1
        now = e
print(cnt)
