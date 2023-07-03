import sys
input = sys.stdin.readline
n = int(input())

flowers = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    flowers.append((a * 100 + b, c * 100 + d))
flowers.sort()

start = 301
end = 301
nxt_end = 301
ans = 0
for s, e in flowers:
    # end를 업데이트할 조건
    if end < s:
        end = nxt_end
        ans += 1

    # next_end를 업데이트
    if end >= s:
        nxt_end = max(nxt_end, e)

    # 1130보다 크다면 종료
    if nxt_end > 1130:
        end = nxt_end
        ans += 1
        break
        
# end이 1130보다 작다면, 0을 출력
if end >= 1130:
    print(ans)
else:
    print(0)