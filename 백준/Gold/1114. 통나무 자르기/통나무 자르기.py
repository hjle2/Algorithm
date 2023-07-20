# 통나무 길이, k 개의 위치 최대 c번
l, k, c = map(int, input().split())
pts = [0, *sorted([*map(int, input().split())]), l]
pieces = [pts[i+1] - pts[i] for i in range(k+1)]
longest = max(pieces)


def solve(mid):
    if longest > mid:
        return 10001, 0
    sum, cnt = 0, 0
    for piece in pieces[::-1]:
        sum += piece
        if sum > mid:
            sum = piece
            cnt += 1
    return cnt, sum if cnt == c else pieces[0]

left, right = 0, l
while left <= right:
    mid = (left + right) // 2
    cnt, front = solve(mid)
    if cnt <= c:
        ans_logest = mid
        ans_front = front
        right = mid - 1
    else:
        left = mid + 1
print(ans_logest, ans_front)

# 9 9 2
# 1 2 3 4 5 6 7 8 9