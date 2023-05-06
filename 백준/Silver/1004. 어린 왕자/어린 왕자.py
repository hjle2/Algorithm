def get_distance(x1, y1, x2, y2):
    x = abs(x1-x2)
    y = abs(y1-y2)
    square = x * x + y * y
    return square ** (1/2)


for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    cnt1 = cnt2 = 0

    n = int(input())
    stars = []
    for _ in range(n):
        x, y, r = map(int, input().split())

        dist1 = get_distance(x1, y1, x, y)
        dist2 = get_distance(x2, y2, x, y)
        # 현재 별의 안에 둘 다 있으면,
        if dist1 < r and dist2 < r:
            continue
        elif dist1 < r:
            cnt1 += 1
        elif dist2 < r:
            cnt2 += 1
    print(cnt1 + cnt2)
