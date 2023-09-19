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


print(get_KMP_table('abbab'))
