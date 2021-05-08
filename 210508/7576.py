from collections import deque
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(M)]
dxy = [(0, -1), (0, 1), (-1, 0), (1, 0)]
Q = deque([])
for i in range(M):
    for j in range(N):
        if box[i][j] == 1:
            Q.append((i,j))

cnt = -1
while Q:
    cnt += 1
    for _ in range(len(Q)):
        x, y = Q.popleft()
        for dx, dy in dxy:
            rx, ry = dx + x, dy + y
            if 0 <= rx < M and 0 <= ry < N:
                if box[rx][ry] == 0:
                    box[rx][ry] = 1
                    Q.append((rx, ry))

if 0 == sum([box[i].count(0) for i in range(M)]):
    print(cnt)
else:
    print(-1)