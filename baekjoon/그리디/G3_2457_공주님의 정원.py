# 모두 같은 해에 피어서 지는 총 N개의 꽃
# 피는 날과 지는 날이 정해져 있다
# 1, 3, 5, 7, 8, 10, 12월은 31일까지, 2월은 28일까지
# 공주가 가장 좋아하는 계절인 3/1부터 11/30까지 매일 꽃이 한 가지 이상 피어있도록 한다
# 정원이 넓지 않으므로 정원에 심는 꽃들의 수를 가능한 적게 한다

n = int(input())
flower = sorted([[*map(int, input().split())]for _ in range(n)])
# 꽃이 지는 시간별로 정렬한다.


# flower뒤에 피는 꽃이 nxt_flower가 되는 것이 가능하면 true 아니면 false
def isPossible(end_date, nxt_start):
    if end_date[0] < nxt_start[0]: # 다음 꽃이 다음 달에 피면 불가능
        return False

    if end_date[0] == nxt_start[0]: # 다음 꽃이 현재 꽃이 지는 달과 같은 달에 피면
        if end_date[1] < nxt_start[1]:
            return False
        else: # 다음 꽃이 피는 달과 현재 꽃이 지는 달이 같고, 다음 꽃이 피는 날짜가 더 이르거나 같으면 다음 꽃이 될 수 있다
            return True
    return True


# j 꽃이 더 늦게 지는지
def is_later_fall(i, j):
    if i == -1:
        return True
    a_flower = flower[i]
    b_flower = flower[j]
    if a_flower[2] < b_flower[2]:
        return True
    if a_flower[2] == b_flower[2]:
        if a_flower[3] < b_flower[3]:
            return True
        else:
            return False
    else:
        return False


# 다음으로 필 수 있는 꽃 중에서 지는 시간이 가장 먼 꽃을 선택한다
def get_next_flower(idx, prev_end):
    ans = -1
    for i in range(idx, n):
        cur_flower = flower[i]
        cur_start = (cur_flower[0], cur_flower[1])

        if not isPossible(prev_end, cur_start):
            return ans
        if is_later_fall(ans, i):
            ans = i
    return ans


def solve():
    if flower[0][0] > 3 or (flower[0][0] == 3 and flower[0][1] > 1): # 3/1부터 피는 꽃이 없으면 0
        return 0
    start_date = (3, 1) # 3/1부터 피어있는 꽃을 찾는다
    idx = -1
    cnt = 0
    while True:
        if start_date[0] > 11: break
        idx = get_next_flower(idx + 1, start_date)
        if idx == -1:
            break
        cnt += 1
        start_date = (flower[idx][2], flower[idx][3])

    if start_date[0] < 12:
        return 0
    return cnt


print(solve())


# 예외상황 3/1, 11/30까지 꽃을 매일 피울 수 없는 경우
# 꽃을 순서대로 정렬
# 시작 날짜를 3/1로 설정
# 시작 날짜로부터 꽃이 지는 날짜가 가장 먼 꽃을 고른다
# 꽃을 순서대로 정렬했기 때문에 더 늦게 지는 꽃인지 확인하여 다음 꽃 인덱스를 갱싱하도록 하는 함수를 사용한다
