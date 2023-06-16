from collections import deque

n, k = map(int, input().split())
m = len(str(n))


def solve():
    ans = 0
    visited = set()
    visited.add((n, 0))

    que = deque([(n, 0)])
    while que:
        cur, cnt = que.pop()
        # k번 연산을 끝낸 숫자 중에서 가장 큰 수가 정답
        if cnt == k:
            ans = max(ans, cur)
            continue

        nums = [*str(cur)]

        # 모든 숫자 교환해서 que에 담아주기
        for i in range(m-1):
            for j in range(i+1, m):
                if i == 0 and nums[j] == '0': continue
                nums[i], nums[j] = nums[j], nums[i]     # 연산 수행하기 위해 숫자 교환하기
                num = int(''.join(nums))                 # 연산 수행 결과를 숫자로 바꾸기
                if (num, cnt + 1) not in visited:        # 연산 결과가 이미 구해져있던 답이라면 중복 계산하지 않기
                    visited.add((num, cnt + 1))
                    que.append((num, cnt + 1))
                # 다음 교환을 위해 다시 되돌리기
                nums[i], nums[j] = nums[j], nums[i]
    print(ans if ans > 0 else -1)                       # ans 가 초기값 0 그대로라면 답이 없다는 의미이므로 -1을 출력해준다

solve()
