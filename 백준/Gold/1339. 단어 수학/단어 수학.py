n = int(input())
words = [[*input()] for _ in range(n)]

arr = [0] * 26                          # 각 알파벳마다의 가중치를 계산하기
A = ord('A')
for word in words:
    l = len(word) - 1
    for i, w in enumerate(word):
        value = 10 ** (l - i)
        arr[ord(w) - A] += value

ans, num = 0, 9                         # 가중치를 기반으로 알파벳에 숫자 부여하기
while True:
    max_value = max(arr)
    if max_value == 0:
        break
    max_idx = arr.index(max_value)
    ans += num * arr[max_idx]
    arr[max_idx] = 0
    num -= 1
print(ans)
