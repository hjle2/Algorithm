n = int(input())
a = [*map(int, input().split())]
b = [*map(int, input().split())]
a.sort()
b.sort(reverse=True)
s = 0
for i in range(n):
    s += a[i] * b[i]
print(s)