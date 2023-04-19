import sys
import heapq

input = sys.stdin.readline

class string:
    def __init__(self, s):
        self.s = s

    def __lt__(self, other):
        if self.s + other.s < other.s + self.s:
            return True
        else:
            return False

    def getString(self):
        return self.s


n = int(input())
word = []
ans = ""
for _ in range(n):
    w = input().strip()
    heapq.heappush(word, string(w))

while word:
    w = heapq.heappop(word).getString()
    ans += w[0]

    if len(w) > 1:
        heapq.heappush(word, string(w[1:]))
print(ans)
