import itertools


def is_candidate_key(columns):
    chk = []
    for r in rel:
        r = list(map(str, r))
        v = ''.join(r[i] for i in columns)
        if v not in chk:
            chk.append(v)
        else:
            return False
    return True


def is_unique(key):
    global keys
    for k in keys:
        tag = True
        for c in k:
            if c not in key:
                tag = False
                break
        if tag: return False
    return True

rel = []
keys = []
def solution(relation):
    global rel
    global keys
    n = len(relation[0])
    answer = 0
    rel = relation

    for i in range(n):
        ar = list(itertools.combinations(range(n), i+1))
        for a in ar:
            if is_unique(a) and is_candidate_key(a):
                keys.append(a)
                answer += 1
    return answer

solution( [['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']])
