import heapq
import sys
input = sys.stdin.readline
n = int(input())

st = [[*map(int, input().split())]for _ in range(n)]
st.sort() # 강의 시작시간 기준으로 정렬

que = [st[0][1]] # 첫번째 강의의 종료 시간
for i in range(1, n):
    if que[0] <= st[i][0]: # 가장 일찍 끝나는 강의 시간보다 더 늦게 시작하면 ㄱㅊ
        heapq.heappop(que)
    heapq.heappush(que, st[i][1]) # 쌓인 강의 수가 필요한 강의실의 수가 된다.
print(len(que)) # 쌓인 강의