# 책을 줄 수 있는 최대 학생 수

# 백준이가 책을 줄 수 있는 최대 학생 수를 출력
def main():
    # N: 갖고 있는 책
    # M: 책을 원하는 학부생
    N, M = map(int, input().split())
    ab = [[*map(int, input().split())] for _ in range(M)]

    chk = [False] * (N + 1)
    # 정렬을 b 를 기준으로 먼저 해야 최대한 많은 학생에게 책을 줄 수 있다!!!
    ab.sort(key=lambda x:(x[1], x[0]))

    ret = 0
    for a, b in ab:
        for i in range(a, b+1):
            if not chk[i]:
                chk[i] = True
                ret += 1
                break
    print(ret)


for _ in range(int(input())):
    main()