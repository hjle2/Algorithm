n = int(input())
min_ar = [0] * 3
max_ar = [0] * 3

min_tmp = [0] * 3
max_tmp = [0] * 3

for i in range(1, n+1):
    a, b, c = map(int, input().split())
    for j in range(3):
        if j == 0:
            min_ar[j] = a + min(min_tmp[0], min_tmp[1])
        elif j == 1:
            min_ar[j] = b + min(min_tmp[0], min_tmp[1], min_tmp[2])
        else:
            min_ar[j] = c + min(min_tmp[1], min_tmp[2])

        if j == 0:
            max_ar[j] = a + max(max_tmp[0], max_tmp[1])
        elif j == 1:
            max_ar[j] = b + max(max_tmp[0], max_tmp[1], max_tmp[2])
        else:
            max_ar[j] = c + max(max_tmp[1], max_tmp[2])
    for i in range(3):
        min_tmp[i] = min_ar[i]
        max_tmp[i] = max_ar[i]

print(max(max_ar), min(min_ar))
