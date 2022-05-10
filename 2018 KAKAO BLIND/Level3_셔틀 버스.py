def gettimestr(h, m):
    h += m//60
    m %= 60
    return '%02d:%02d'%(h, m)

def get1minealier(txt):
    h, m = txt.split(':')
    h, m = int(h), int(m)
    m -= 1
    h += m//60
    m = m%60
    return gettimestr(h, m)

def solution(n, t, m, timetable):
    len_line = len(timetable)
    ar = [[]for _ in range(n)]
    timetable.sort()

    H, M = 9, 0
    i_bus = 0
    bus_time = gettimestr(H, M)
    seat = m
    i = 0
    while i < len(timetable):
        arv = timetable[i]
        if bus_time >= arv and seat > 0:
            ar[i_bus].append(i)
            seat -= 1
            i += 1
        else:
            i_bus += 1
            if i_bus == n: break
            seat = m
            M += t
            bus_time = gettimestr(H, M)

    if ar[n-1] and len(ar[n-1]) == m:
        return get1minealier(timetable[ar[n - 1].pop()])
    else: return bus_time

