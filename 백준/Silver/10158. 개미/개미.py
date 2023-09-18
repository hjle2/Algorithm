W, H = map(int, input().split())
P, Q = map(int, input().split())
T = int(input())

x = (P + T) % (2 * W)
y = (Q + T) % (2 * H)

if x > W:
    x = 2 * W - x

if y > H:
    y = 2 * H - y

print(x, y)