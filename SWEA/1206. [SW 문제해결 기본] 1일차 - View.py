# 왼, 오 창문을 열었을 때 양쪽 모두 2 이상! 의 공간
# 맨 왼쪽 두칸과 오른쪾 두칸은 건물이 없다
# 최대 높이는 255

def sunlight():
    ans = 0
    for i in range(2, n-2):
        h = a[i]
        other = max(a[i-2],a[i-1],a[i+1],a[i+2])
        ans += h-other if h>other else 0
    return ans


for t in range(10):
    n = int(input())
    a = list(map(int, input().split()))
    print(f'#{t+1}', sunlight())
