a = [*map(int, input().split())]

for i in range(3):
    for j in range(i+1, 3):
        a.append(a[i] * a[j])
        for k in range(j+1, 3):
            a.append(a[i] * a[j] * a[k])

ans = 0
odd = False
for n in a:
    if n%2 == 1:
        if odd:
            ans = max(ans, n)
        else:
            ans = n
            odd = True
    else:
        if odd:
            continue
        else:
            ans = max(ans, n)
print(ans)
