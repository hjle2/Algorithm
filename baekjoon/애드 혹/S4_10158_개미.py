import sys
input = sys.stdin.readline

W, H = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
p = (t + p) % (2 * W)
q = (t + q) % (2 * H)
if p > W: p = W - (p - W)
if q > H: q = H - (q - H)
print(p, q)
print(p, q)
