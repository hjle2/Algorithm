import sys
input = sys.stdin.readline
n, k = map(int, input().split())
names = [input().rstrip() for _ in range(n)]
length_cnt = [0] * 21
for i in range(k):
    length_cnt[len(names[i])] += 1

ans = 0
for i in range(n-1):
    if i + k < n:
        length_cnt[len(names[i+k])] += 1
    ans += length_cnt[len(names[i])] - 1
    length_cnt[len(names[i])] -= 1

print(ans)