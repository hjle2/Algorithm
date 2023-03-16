n, k = map(int, input().split())
appliance = [*map(int, input().split())]

cnt = 0
tap = []


def get_next_app(idx, tap):
    nxt_idx = []
    for tap_idx, tap_app in enumerate(tap):
        if tap_app not in appliance[idx:]:
            return tap_idx

        else:
            nxt_idx.append((-appliance[idx:].index()))


for idx, app in enumerate(appliance):
    # tap에 꽂혀있으면 꽂혀있는데로 사용
    if app in tap:
        continue
    # tap에 자리가 남아있으면 남는 자리에 꽂아서 사용
    if len(tap) < n:
        tap.append(app)
        continue
    # 꽂힌 전자기기 중에 가장 나중에 사용되는 전자기기를 뽑는다.
    # 나중에 사용되지 않는 전자기기를 뽑는다
    pull_idx = get_next_app(idx, tap)

    del tap[pull_idx]
    tap.append(app)
    cnt += 1

print(cnt)
