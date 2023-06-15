import sys
input = sys.stdin.readline
n = int(input())
start, end = [], []
for i in range(n):
    s, e = map(int, input().split())
    start.append(s)
    end.append(e)

start.sort()
end.sort()
ans = n
end_idx = 0
for i in range(n):
    if start[i] >= end[end_idx]:
        ans -= 1
        end_idx += 1
print(ans)