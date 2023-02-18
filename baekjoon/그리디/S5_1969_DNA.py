# DNA 는 서로 다른 4가지의 뉴클레오티드로 이루어져 있다
# (Adenine, Thymine, Guanine, Cytonine)
# 어떤 DNA를 표현할 때 이 뉴클레오티드의 첫글자로 표현한다
# Hamming Distance란  길이가 같은 DNA가 있을 때 각 위치의 뉴클리오티드 문자가 다른 것의 갯수 이다

# N개의 길이 M인 DNA 가 주어질 때 Hamming Distance 의 합이 가장 작은 DNA를 구하는 것이다

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
DNAs = [[*input()][:-1]for _ in range(N)]
key = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
cnt = [[0] * 4for _ in range(M)]
for dna in DNAs:
    for i, n in enumerate(dna):
        cnt[i][key[n]] += 1
ans, ansc = '', 0
for i in range(M):
    idx = cnt[i].index(max(cnt[i]))
    ans += ['A', 'C', 'G', 'T'][idx]
    ansc += sum(cnt[i]) - cnt[i][idx]
print(ans, ansc, sep='\n')