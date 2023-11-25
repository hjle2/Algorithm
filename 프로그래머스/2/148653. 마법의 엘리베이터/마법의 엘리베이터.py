import math
def solution(storey):
    return get_count(storey, 10 ** (int(math.log(storey, 10) + 1)))


def get_count(cur, step):
    cur = abs(cur)
    if step == 1:
        return abs(cur)
    
    else:
        cnt = cur // step
        ret = cnt + get_count(cur - cnt * step, step // 10)
        cnt += 1
        ret = min(ret, cnt + get_count(cur - cnt * step, step // 10))
        return ret