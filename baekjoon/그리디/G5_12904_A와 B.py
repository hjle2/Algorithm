# 두 문자열이 주어졌을 때 1 문자열을 2로 바꾸는 게임
# 연산은
# 문자열 뒤에 A를 추가한다
# 문자열을 뒤집고 뒤에 B를 추가한다
# 이 두 가지 연산만 가능하다
# 바꿀 수 있으면 1 없으면 0 출력

A = [*input()]
B = [*input()]
cnt = len(B) - len(A)

while cnt:
    cnt-=1
    c = B.pop()
    if c == 'B':
        B.reverse()

print(1 if A == B else 0)