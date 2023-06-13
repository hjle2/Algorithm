inp = input().split('-')
ans = sum(map(int, inp[0].split('+')))
for sik in inp[1:]:
    ans -= sum(map(int, sik.split('+')))
print(ans)