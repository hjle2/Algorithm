n = int(input())
l, r = 1, 2
ans = []

while l < r:
    tmp = r * r - l * l
    if tmp == n:
        ans.append(r)
    if tmp < n:
        r += 1
    else:
        l += 1

ans.sort()
print(-1) if not ans else print(*ans, sep='\n')