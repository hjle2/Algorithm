# N 개의 로프
# 각각의 로프는 굵기나 길이가 다르기 때문에 들 수 있는 물체의 중량이 서로 다르다
# 로프를 병렬로 연결하면 각각의 로프에 걸리는 중량을 나눌 수 있다
# 로프들을 이용해 들어 올릴 수 있는 최대 중량을 구하라
# 모든 로프를 사용할 필요는 없다
import sys
input = sys.stdin.readline

def solve():
    ans = 0
    for i in range(N):
        if W[i]*(i+1) >= ans:
            ans = W[i] * (i+1)
    return ans
    
    
N = int(input())
W = [int(input())for _ in range(N)]
W.sort(reverse=True)
print(solve())
#  if 아래에 else 를 추가하여
# break 해주었는데 만약, 
# 5 4 1 1 1 1
# 과 같이 끝까지 모드 로프가 함께 중량을 들었을 때가 정답인 케이스가 있을 수 있다는 점을 간과했음..
