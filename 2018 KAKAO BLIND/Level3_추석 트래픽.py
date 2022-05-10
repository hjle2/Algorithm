def solution(lines):
    N = len(lines)
    max_t = 24 * 60 * 60 * 1000 + 1
    graph = [0]*max_t
    t_max = 0
    t_min = max_t - 1

    for i in range(N):
        _, time, period = lines[i].split()
        h,m,s = time.split(':')
        h, m, s, period = int(h), int(m), float(s), float(period[:-1]) * 1000
        end_t = (h * 60 + m) * 60 + s
        end_t = int(end_t * 1000)
        stt_t = end_t - int(period) + 1 - 1000 + 1

        stt_t, end_t = max(stt_t, 0), end_t


        for t in range(stt_t, end_t + 1):
            graph[t] += 1
        # print(stt_t, end_t)

        # graph[stt_t] += 1
        # graph[end_t + 1] -= 1

        # t_max = max(t_max, end_t)
        # t_min = min(t_min, stt_t)

    # for i in range(t_min, t_max):
    #     graph[i] += graph[i-1]
    return max(graph)
