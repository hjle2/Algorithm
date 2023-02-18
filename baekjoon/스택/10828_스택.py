import sys


class Stack:
    def __init__(self):
        self.ar = []
    def push(self, x):
        self.ar.append(x)
    def pop(self):
        return self.ar.pop() if self.ar else -1
    def size(self):
        return len(self.ar)
    def empty(self):
        return 0 if self.ar else 1
    def top(self):
        return self.ar[-1] if  self.ar else -1

st = Stack()
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    cm = input().split()
    if len(cm) == 2:
        st.push(cm[1])
    elif cm[0] == 'top':
        print(st.top())
    elif cm[0] == 'size':
        print(st.size())
    elif cm[0] == 'pop':
        print(st.pop())
    elif cm[0] == 'empty':
        print(st.empty())
