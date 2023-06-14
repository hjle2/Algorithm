import sys
input = sys.stdin.readline

def solve():
    applicant.sort()

    ans = 0
    tmp = applicant[0][1]
    for a, b in applicant:
        if b <= tmp:
            ans += 1
            tmp = b
    print(ans)


for _ in range(int(input())):
    n = int(input())
    applicant = [[*map(int, input().split())]for _ in range(n)]
    solve()