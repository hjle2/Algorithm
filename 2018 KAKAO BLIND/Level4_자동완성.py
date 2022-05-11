# # 한 번 입력된 문자열은 학습되어 첫 글자만 입력해도 다음 글자들을 추천해 준다.
# # 앞부분이 같은 경우에는 다른 문제가 나올 때 까지 입력을 해야 한다.
#
# def get_equal_len(word, compare):
#     n = min(len(word), len(compare))
#     for i in range(n):
#         if word[i] != compare[i]:
#             return i
#     return n
#
# ar = []
#
# def make_ar(words):
#     global ar
#     N = len(words)
#     ar = [[0]*N for _ in range(N)]
#
#     for i in range(N-1):
#         # cnt = 0
#         word = words[i]
#         for j in range(i+1, N):
#             e_len = get_equal_len(word, words[j])
#             # cnt = max(cnt, e_len)
#             ar[i][j] = min(len(word), e_len+1)
#             ar[j][i] = min(len(words[j]), e_len+1)
#
# def solution(words):
#     N = len(words)
#     answer = 0
#     global ar
#     # for i in range(N):
#     #     cnt = 0
#     #     word = words[i]
#     #     for j in range(N):
#     #         if i == j: continue
#     #         e_len = get_equal_len(word, words[j])
#     #         if cnt < e_len:
#     #             cnt = e_len
#     #     answer += min(len(word), cnt + 1)
#     make_ar(words)
#     for i in range(N):
#         answer += max(ar[i])
#     return answer
#

ar = {}
def make_ar(words):
    global ar
    N = len(words)
    for i in range(N):
        v = ar
        for c in words[i]:
            if c not in v.keys():
                v[c] = [1, {}]
            else: v[c][0] += 1
            v = v[c][1]



def solution(words):
    answer = 0
    make_ar(words)
    global ar
    for word in words:
        v = ar
        cnt = 0
        for w in word:
            if v[w][0] == 1:
                break
            if w in v.keys():
                cnt += 1
            v = v[w][1]
        answer += min(len(word), cnt + 1)
    return answer


solution(["go","gone","guild"])