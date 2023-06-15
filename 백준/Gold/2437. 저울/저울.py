def solve():
    s = 0
    for c in chu:
        if s + 1 < c:
            print(s+1)
            return
        s += c
    print(s+1)
    

n = int(input())
chu = [*map(int, input().split())]
chu.sort()

solve()