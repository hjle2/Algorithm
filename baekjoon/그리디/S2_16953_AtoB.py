# 정수 A 를 B 로 바꾸려고 한다
# 가능한 연산은 *2, *10 + 1
# 필요한 연산의 최솟값을
import sys
input = sys.stdin.readline

A, B = map(int, input().split())
cnt = 0
while A < B:
    if B%10 == 1:
        B //= 10
    elif B%2 == 0:
        B //= 2
    else: break
    cnt+=1
if A == B:
    print(cnt+1)
else:
    print(-1)
