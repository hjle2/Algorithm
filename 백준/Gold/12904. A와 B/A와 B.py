A = [*input()]
B = [*input()]

ans = 0
while True:
    if A == B:
        ans = 1
        break
    if len(A) == len(B):
        break
    if B[-1] == 'B':
        del B[-1]
        B = B[::-1]
    else:
        del B[-1]
print(ans)