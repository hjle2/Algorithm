def solve():
    cnt = len(t) - len(s)
    while cnt:
        cnt-=1
        c = t.pop() # t의 맨 뒤글자를 비교
        if c == 'B': # B라면 문자의 순서를 뒤집는다
            t.reverse()

s = [*input()]
t = [*input()]

solve()
print(1 if s == t else 0) # 두 문자의 길이가 같아졌을 때 같은 문자라면 1 아니면 0