import math


def solution(fees, records):
    answer = []
    in_time = {}
    out_time = {}
    for record in records:
        t,num,in_out = record.split()
        h,m = t.split(':')
        t = int(h) * 60 + int(m)
        if in_out == 'IN':
            if num in out_time.keys():
                t -= out_time[num]-in_time[num]
                del out_time[num]
            in_time[num] = t
        else:
            out_time[num] = int(h) * 60 + int(m)

    max_t = 23*60+59
    for n in sorted(in_time.keys()):
        fee = fees[1]
        in_t = in_time[n]
        out_t = max_t if n not in out_time.keys() else out_time[n]
        stay = out_t - in_t
        if stay > fees[0]:
            fee += math.ceil((stay-fees[0])/fees[2]) * fees[3]
        answer.append(fee)
    return answer

solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])