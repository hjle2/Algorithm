import sys
input = sys.stdin.readline
n, d, k, c = map(int, input().split())
shusi = [int(input()) for _ in range(n)]

eaten = [0] * (d+1) # 먹은 초밥을 체크할 배열
eaten[c] = 1        # 쿠폰으로 초밥을 먹음

cnt = 1             # 먹은 초밥의 가짓수
for i in range(k):
    if not eaten[shusi[i]]:
        cnt += 1
    eaten[shusi[i]] += 1

ans = cnt
for i in range(n):
    ans = max(ans, cnt)

    eaten[shusi[i]] -= 1
    if not eaten[shusi[i]]:
        cnt -= 1

    if not eaten[shusi[(i + k) % n]]:
        cnt += 1
    eaten[shusi[(i + k) % n]] += 1

print(ans)