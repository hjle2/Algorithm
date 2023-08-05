t = int(input())

for _ in range(t):  
    floor = int(input())
    ho = int(input())
    f0 = [x for x in range(1, ho + 1)]
    for k in range(floor):
        for i in range(1, ho):
            f0[i] += f0[i-1]
    print(f0[-1])