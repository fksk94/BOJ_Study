from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())

if N == 1:
    print(1)
else:
    Q = deque([i for i in range(2, N + 1, 2)])
    if N % 2:
        cnt = 1
    else:
        cnt = 0
    while len(Q) != 1:
        if cnt % 2:
            Q.append(Q.popleft())
            cnt += 1
        else:
            Q.popleft()
            cnt += 1
    print(Q[0])