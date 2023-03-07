# 캠핑장은 연속하는 20일 중 10일동안만 사용할 수 있습니다.

c = 1
while True:
    l, p, v = map(int, input().split())

    if l == 0: break
    ans = v // p * l + min(v % p, l)
    print(f'Case {c}: {ans}')
    c += 1