n = int(input())
meeting = [[*map(int, input().split())]for _ in range(n)]
meeting.sort(key=lambda x:(x[1], x[0]))

prv = 0
ans = 0
for i in range(n):
    s, e = meeting[i]
    if s < prv: continue
    ans += 1
    prv = e
print(ans)