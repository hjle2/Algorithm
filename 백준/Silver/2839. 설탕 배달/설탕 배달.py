N = int(input())
ans = 0
if N in [4, 7]:
    print(-1)
    exit()
while N % 5:
    ans += 1
    N -= 3
ans += N//5
print(ans)