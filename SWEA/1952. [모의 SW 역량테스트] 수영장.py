#  가장 적은 비용
# 1일, 1달 (매달 1일 시작)
# 3달 (다음 해의 이용권만 구매 가능
# 1년 이용권
def dfs(n, d, m, m3):
    ret = ty
    while n < 12 and plan[n]==0:
        n += 1

    if n >= 12:
        return min(ret, d*td + m*tm + m3*tm3)

    v = plan[n]
    if v*td < tm:
        ret = min(ret, dfs(n+1, d+v, m, m3))
    else:
        ret = min(ret, dfs(n+1, d, m+1, m3))
    ret = min(ret, dfs(n+3, d, m, m3+1))
    return ret


for t in range(int(input())):
    td, tm, tm3, ty = map(int, input().split())
    plan = list(map(int, input().split()))
    print(f'#{t+1}', dfs(0, 0, 0, 0))

