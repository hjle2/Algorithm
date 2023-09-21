def get_KMP_table(pattern):
    length = len(pattern)
    kmp_table = [0] * length

    i = 0
    for j in range(1, length):
        if i > 0 and pattern[i] != pattern[j]:
            i = kmp_table[i-1]

        if pattern[i] == pattern[j]:
            i += 1
            kmp_table[j] = i
    return kmp_table


def KMP(word, pattern):
    ret = []
    i = 0
    table = get_KMP_table(pattern)
    for j in range(len(word)):
        while i > 0 and pattern[i] != word[j]:
            i = table[i-1]
    
        if pattern[i] == word[j]:
            i += 1
            if i == len(pattern):
                ret.append(j - i + 1)
                i = table[i-1]
    return ret
