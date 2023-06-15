n, k = map(int, input().split())
apps = [*map(int, input().split())]

ans, plug = 0, []
for i in range(k):
    app = apps[i]
    if app in plug:     # 이미 꽂혀 있다면 패스
        continue
    if len(plug) < n:   # 아직 꽂을 자리가 남아있다면 꽂음
        plug.append(app)
        continue

    # 빼야하는 경우
    # 1. 다시 사용하지 않는 전기용품을 뺀다.
    # 2. 다음 사용이 가장 멀리 있는 전기용품을 뺀다.
    max_idx = 0
    for j in range(n):
        if plug[j] not in apps[i+1:]:
            max_idx = apps.index(plug[j])
            break
        max_idx = max(max_idx, apps[i+1:].index(plug[j]) + i + 1)
    pull_app = apps[max_idx]
    plug[plug.index(pull_app)] = app
    ans += 1
print(ans)
