import sys
r=sys.stdin.readline

def solution(id_list, reports, k):
    N=len(id_list)
    answer = [0]*N
    reported = [[]for _ in range(N)]
    idx={}
    for i,id in enumerate(id_list):
        idx[id]=i

    for re in reports:
        a,b=re.split()
        b=idx[b]
        if not a in reported[b]:
            reported[b].append(a)

    for l in reported:
        if len(l)>=k:
            for id in l:
                answer[idx[id]]+=1
    return answer