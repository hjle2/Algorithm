n = int(input())
ar = [*map(int, input().split())]
ar.sort()

time = 0
ans = 0

for num in ar:
    time += num
    ans += time
print(ans)