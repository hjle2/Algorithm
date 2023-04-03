n, k = map(int, input().split())
hater = []
for _ in range(k):
    a, b = map(int, input().split())
    hater.append((min(a, b), max(a, b)))

hater.sort(key=lambda x:x[1])
cnt = 0
prv_end, start, end = 0, 0, 0

for i, (a, b) in enumerate(hater):
    # 한 컷 더 찍어야 하는 경우
    if prv_end < a:
        cnt += 1
        prv_end = max(b-1, end)
        start = b
    # 이어서 찍을 수 있는 경우
    end = b
if prv_end != end:
    cnt += 1
print(cnt)
