# 탱크는 4방 이동
# 탱크가 위치한 행과 열을 보호한다
# 두 탱크가 같은 칸에 있을 수 없다 -> 중요
# 탱크가 모든 행과 열을 보호하게 배치를 바꾼다
# 탱크가 움직이는 횟수를 '최소화'

n = int(input())
tank = [[]for _ in range(n)]
tank[0] = [0, 0, 0]
for i in range(n):
    r, c = map(int, input().split())
    tank[i] = [r-1, c-1, i]
tank.sort()

ans, ans_str = 0, ''

for i in range(n):
    r = tank[i][0]
    while r > i:
        ans += 1
        ans_str += str(tank[i][2]+1) + ' U\n'
        r -= 1
for i in range(n-1, -1, -1):
    r = tank[i][0]
    while r < i:
        ans += 1
        ans_str += str(tank[i][2]+1) + ' D\n'
        r += 1

tank.sort(key=lambda x:x[1])
for i in range(n):
    c = tank[i][1]
    while c > i:
        ans += 1
        ans_str += str(tank[i][2]+1) + ' L\n'
        c -= 1
for i in range(n-1, -1, -1):
    c = tank[i][1]
    while c < i:
        ans += 1
        ans_str += str(tank[i][2]+1) + ' R\n'
        c += 1
print(ans)
print(ans_str)
