def makeset(str):
    l = {}
    for s in range(len(str) - 1):
        if 'A' <= str[s] <= 'Z' and 'A' <= str[s + 1] <= 'Z':
            key = str[s:s + 2]
            l[key] = 1 if not key in l else l[key] + 1
    return l


def solution(str1, str2):
    answer = 0

    l1, l2 = makeset(str1.upper()), makeset(str2.upper())
    joint = list(set(l1.keys()) | set(l2.keys()))
    inter = len(list(set(l1.keys()) & set(l2.keys())))
    n_joint = len(joint)

    for l in joint:
        if l in l1.keys() and l1[l] > 1 and l in l2.keys() and l2[l] > 1:
            inter += min(l1[l], l2[l]) - 1
            n_joint += max(l1[l], l2[l]) - 1
        elif l in l1.keys() and l1[l] > 1:
            n_joint += l1[l] - 1
        elif l in l2.keys() and l2[l] > 1:
            n_joint += l2[l] - 1

    if n_joint > 0:
        answer = inter / n_joint
    else:
        answer = 1

    return int(answer * 65536)