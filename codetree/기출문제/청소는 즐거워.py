n = int(input())
ar = [[*map(int, input().split())] for _ in range(n)]
r = c = n // 2

d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
five = [[[0, -2]], [[2, 0]], [[0, 2]], [[-2, 0]]]
ten = [[[-1, -1], [1, -1]], [[1, -1], [1, 1]], [[1, 1], [-1, 1]], [[-1, 1], [-1, -1]]]
seven = [[[1, 0], [-1, 0]], [[0, 1], [0, -1]], [[1, 0], [-1, 0]], [[0, 1], [0, -1]]]
two = [[[2, 0], [-2, 0]], [[0, 2], [0, -2]], [[2, 0], [-2, 0]], [[0, 2], [0, -2]]]
one = [[[1, 1], [-1, 1]], [[-1, -1], [-1, 1]], [[-1, -1], [1, -1]], [[1, -1], [1, 1]]]



def in_range(r, c):
    return 0 <= r < n and 0 <= c < n


def brush(r, c, d, dust):
    sub, out = dust, 0

    for dx, dy in five[d]:
        nr, nc = r + dx, c + dy
        tmp = dust // 20
        sub -= tmp
        if not in_range(nr, nc):
            out += tmp
            continue
        ar[nr][nc] += tmp

    for dx, dy in ten[d]:
        nr, nc = r + dx, c + dy
        tmp = dust // 10
        sub -= tmp
        if not in_range(nr, nc):
            out += tmp
            continue
        ar[nr][nc] += tmp

    for dx, dy in seven[d]:
        nr, nc = r + dx, c + dy
        tmp = dust * 7 // 100
        sub -= tmp
        if not in_range(nr, nc):
            out += tmp
            continue
        ar[nr][nc] += tmp

    for dx, dy in two[d]:
        nr, nc = r + dx, c + dy
        tmp = dust // 50
        sub -= tmp
        if not in_range(nr, nc):
            out += tmp
            continue
        ar[nr][nc] += tmp

    for dx, dy in one[d]:
        nr, nc = r + dx, c + dy
        tmp = dust // 100
        sub -= tmp
        if not in_range(nr, nc):
            out += tmp
            continue
        ar[nr][nc] += tmp

    return sub, out




ret = 0
dist = 1
while True:
    for i in range(dist):
        r, c = r + d[0][0], c + d[0][1]

        dust = ar[r][c]
        ar[r][c] = 0

        dust, out = brush(r, c, 0, dust)
        ret += out

        if r == 0 and c == 0:
            ret += dust
            break
        nr, nc = r + d[0][0], c + d[0][1]
        if in_range(nr, nc):
            ar[nr][nc] += dust
        else:
            ret += dust

    if r == 0 and c == 0:
        break

    for i in range(dist):
        r, c = r + d[1][0], c + d[1][1]
        dust = ar[r][c]
        ar[r][c] = 0

        dust, out = brush(r, c, 1, dust)
        ret += out
        nr, nc = r + d[1][0], c + d[1][1]
        if in_range(nr, nc):
            ar[nr][nc] += dust
        else:
            ret += dust

    dist += 1

    for i in range(dist):
        r, c = r + d[2][0], c + d[2][1]
        dust = ar[r][c]
        ar[r][c] = 0


        dust, out = brush(r, c, 2, dust)
        ret += out
        nr, nc = r + d[2][0], c + d[2][1]
        if in_range(nr, nc):
            ar[nr][nc] += dust
        else:
            ret += dust

    for i in range(dist):
        r, c = r + d[3][0], c + d[3][1]
        dust = ar[r][c]
        ar[r][c] = 0


        dust, out = brush(r, c, 3, dust)
        ret += out
        nr, nc = r + d[3][0], c + d[3][1]
        if in_range(nr, nc):
            ar[nr][nc] += dust
        else:
            ret += dust

    dist += 1

print(ret)
