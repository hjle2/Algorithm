import sys
si = sys.stdin.readline


def solve():
    # 모두와 비교했을 떄 두 등수 모두 낮은 경우가 있으면 탈락
    # 즉, 두 성적 중 하나라도 누군가보다 높으면 합격
    # 서류성적을 기준으로 sort되어있기 때문에 면접성적만을 비교하면 된다
    cnt = 1
    compare = man[0][1] # 등수가 가장 높은 사람의 면접 성적
    for a, b in man[1:]:
        if b < compare: # 면접성적이 서류 성적 높은 사람의 성적보다 높음 -> 합격
            cnt += 1
            compare = b
    return cnt


for _ in range(int(si())):
    n = int(si())
    man = sorted([[*map(int, si().split())]for _ in range(n)]) # 성적
    print(solve())