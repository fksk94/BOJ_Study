from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
Q = deque([])

for i in range(N):
    a = list(input().split())
    if a[0] == 'push_back':
        Q.append(a[1])
    elif a[0] == 'push_front':
        Q.appendleft(a[1])
    elif a[0] == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if Q:
            print(Q[-1])
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(Q))
    elif a[0] == 'empty':
        if Q:
            print(0)
        else:
            print(1)
    elif a[0] == 'pop_front':
        if Q:
            print(Q.popleft())
        else:
            print(-1)
    elif a[0] == 'pop_back':
        if Q:
            print(Q.pop())
        else:
            print(-1)
