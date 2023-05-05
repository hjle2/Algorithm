def get_distance(x1, y1, x2, y2):
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    square = x * x + y * y

    return square ** (1/2)


for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        dist = get_distance(x1, y1, x2, y2)
        if r1 + r2 == dist:
            print(1)
        elif r1 + r2 < dist:
            print(0)
        elif r1 + r2 > dist:
            r1, r2 = max(r1, r2), min(r1, r2)
            if r1 > dist + r2:
                print(0)
            elif r1 == dist + r2:
                print(1)
            else:
                print(2)

