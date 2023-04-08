n, l = map(int, input().split())

spot = [[*map(int, input().split())]for _ in range(n)]
spot.sort()

end = 1
cnt = 0
for s, e in spot:
    if s < end:
        s = end
        if s >= e: continue

    need_l = e - s

    tmp_cnt = need_l // l
    if need_l % l > 0:
        tmp_cnt += 1
    end = s + tmp_cnt * l
    cnt += tmp_cnt

print(cnt)
