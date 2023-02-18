# 원판이 큰 순서대로 쌓여 있다.
# 한 번에 한개만 옮길 수 있다.
# 항상 위의 것이 아래 것 보다 작다.
# 위의 규칙을 따라 첫번째 장대에서 세번째 장대로 옮겨야 한다.
# 이동 횟수의 최소 값을 구하라

def solve(n, frm, to):
    if n == 1:
        print(frm, to)
        return
    solve(n-1, frm, 6-frm-to)
    print(frm, to)
    solve(n-1, 6-frm-to, to)


# N 1<=N<=20
N = int(input())
# 가장 큰 N 원판을 제외한 모든 원판을 3이 아닌 2로 옮겨야 함!
print(2**N-1)
solve(N, 1, 3)