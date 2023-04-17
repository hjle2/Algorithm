# 레이스 트랙의 길이 n
# 심팜 m명을 배치
# 가장 가까운 두 심판의 거리를 최대로

n, m, k = map(int, input().split())
referee = [*map(int, input().split())]

def getRet(gap):
    ret = []
    cnt = 0
    limit = 0
    for i in range(k):
        if limit <= referee[i]:
            cnt+=1
            limit = referee[i] + gap
            ret.append('1')

            if cnt == m:
                while len(ret) != len(referee):
                    ret.append('0')
                break
        else:
            ret.append('0')

    if cnt == m:
        return ret
    return []


def solve():
    ans = ['0'] * k
    if m == 2:
        ans[0] = ans[-1] = '1'
        return ans
    if m == k:
        ans = ['1'] * k
        return ans


    left, right = 0, n
    tmp_ret = []
    ret = []
    while left <= right:
        mid = (left + right) // 2

        tmp_ret = getRet(mid)

        if len(tmp_ret) != 0:
            left = mid + 1
            ret = tmp_ret
        else:
            right = mid - 1
            
    return ret

print(''.join(solve()))