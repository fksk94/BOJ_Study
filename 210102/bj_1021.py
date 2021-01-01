from sys import stdin
from collections import deque

input = stdin.readline

N, M = map(int, input().split())
Q = deque([i for i in range(1, N+1)])
vals = list(map(int, input().split()))
cnt = 0
for i in vals:
    idx = Q.index(i)
    while True:
        if idx > (N-1)//2:
            tmp = Q.pop()
            if tmp != i:
                cnt += 1
                Q.appendleft(tmp)
            else:
                cnt += 1
                N -= 1
                break
        else:
            tmp = Q.popleft()
            if tmp != i:
                cnt += 1
                Q.append(tmp)
            else:
                N -= 1
                break
print(cnt)
