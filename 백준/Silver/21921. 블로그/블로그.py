n, x = map(int, input().split())
visitors = [*map(int, input().split())]
cnt = 0
for i in range(x-1):
    cnt += visitors[i]

ans, ans_cnt = 0, 0
for i in range(n-x+1):
    cnt += visitors[i+x-1]
    if ans < cnt:
        ans = cnt
        ans_cnt = 1
    elif ans == cnt:
        ans_cnt += 1
    cnt -= visitors[i]

if ans > 0:
    print(ans, ans_cnt, sep='\n')
else:
    print('SAD')