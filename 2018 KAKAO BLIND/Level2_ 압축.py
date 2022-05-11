# LZW 알고리즘
# 길이가 1인 모든 단어를 포함하도록 사전을 초기화
# 현재 입력과 일치하는 가장 긴 문자열을 찾는다.
# 색인 번호를 출력하고 입력에서 제거
# 입력에서 처리되지 않은 글자가 남으면 이 글자를 위의 긴 문자열과 합쳐 사전에 등록

# A 1 ... Z 26
# ord - 64

ar = [chr(i) for i in range(64, 64 + 27)]

def solution(msg):
    answer = []
    i = 0
    while i < len(msg):
        c = msg[i]
        j = i
        w = c
        j += 1
        while w in ar and j < len(msg):
            w += msg[j]
            j += 1
        tmp = w
        if w not in ar:
            w = w[:-1]
        answer.append(ar.index(w))
        ar.append(tmp)

        i += len(w)

    return answer

solution('KAKAO')