import sys
input = sys.stdin.readline

a, b = map(int, input().split())

# b->a로 생각
# b의 끝자리가 1이 아니면 /2
cnt = 0
while a != b and a < b:
    if b%10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    else:
        break
    cnt += 1
print(cnt+1 if a == b else -1)