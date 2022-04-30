for k in range(100):
    n = 1
    for i in range(31, -1, -1):
        n *= n
        if k & (1<<i):
            n *= 2
    print(n)
