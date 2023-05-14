for _ in range(int(input())):
    n, m = map(int, input().split())
    ans = 1
    m1, m2 = 1, 2
    while True:
        if m1 % m == 1 and m2 % m == 1:
            break
        ans += 1
        m1, m2 = m2, (m1 + m2) % m

    print(n, ans)
