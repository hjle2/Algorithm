n, k = map(int, input().split())
numbers = [*input().rstrip()]

ans, org_k = [], k
for num in numbers:
    while k > 0 and ans and ans[-1] < num:
        ans.pop()
        k -= 1
    ans.append(num)
print(*ans[:n-org_k], sep='')
