from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())

rcnt = 0

for _ in range(N):
    N, M = map(int, input().split())
    Q = deque(zip(list(map(int, input().split())), range(N)))
    cnt = 0
    while Q:
        max_Q, garbage = max(Q)
        tmp, idx = Q.popleft()
        if tmp == max_Q:
            cnt += 1
            if idx == M:
                break
        else:
            Q.append((tmp, idx))
    print(cnt)