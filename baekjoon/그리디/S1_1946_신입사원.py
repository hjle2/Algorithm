# 신입사원을 선발하고자 한다
# 다른 모든 지원자와 비교했을 때 서류, 면접 점수 모두 떨어진다면 선발되지 않는다
# 적어도 하나가 모든 다른 지원자보다 높으면 합격
# 선발할 수 있는 신입사원의 최대 인원수를 구하라
import sys
input = sys.stdin.readline

def solve():
    cnt = 1
    compare = ap[0][1]
    for a, b in ap[1:]:
        if b < compare:
            cnt+= 1
            compare = b
    print(cnt)

for _ in range(int(input())):
    N = int(input())
    # 서류 성적 순위, 면접 성적 순위
    ap = [[*map(int, input().split())]for _ in range(N)]
    ap.sort()
    solve()
