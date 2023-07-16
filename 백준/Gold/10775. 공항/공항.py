import sys
input = sys.stdin.readline
g = int(input())
p = int(input())
gate_parent = [*range(g+1)]


def find_parent(plane):
    if gate_parent[plane] == plane:
        return plane
    gate_parent[plane] = find_parent(gate_parent[plane])
    return gate_parent[plane]


ans = 0
for _ in range(p):
    plane = int(input())
    parent = find_parent(plane)

    if parent == 0:
        break

    gate_parent[parent] = gate_parent[parent-1]
    ans += 1
print(ans)