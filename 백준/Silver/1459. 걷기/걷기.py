# 도시의 크기는 무한대
# 도시의 세로 도로는 모든 x좌표마다
# 도시의 가로 도로는 모든 y좌표마다


# 집의 위치 x, y
# 가로, 세로로 건너는 시간 w
# 대각선으로 가로지르는데 걸리는 시간 s
x, y, w, s = map(int, input().split())

if w * 2 < s: # 가로, 세로로 두번 건너는 시간이 대각선으로 가로지는 것 보다 빠르면
    print(x * w + y * w)
else: # 대각선이 더 빠르면, 대각선으로 최대한 많이 이동한 후 가로, 세로로 이동
    xx = min(x, y)
    ans = xx * s
    x -= xx; y -= xx
    if w > s:
        ans += x//2 * s * 2 + y // 2 * s * 2 + x % 2 * w + y % 2 * w
    else:
        ans += (x + y) * w
    print(ans)

