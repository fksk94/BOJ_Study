from collections import deque
from itertools import combinations
from sys import stdin
input = stdin.readline

dxy = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(com):
    res = 0
    Q = deque(com)
    visit = [[False] * N for i in range(N)]
    for i, j in Q:
        visit[i][j] = True
    cnt = 0
    while Q:
        cnt += 1
        for _ in range(len(Q)):
            x, y = Q.popleft()
            for nx, ny in dxy:
                rx = x + nx
                ry = y + ny
                if 0 <= rx < N and 0<= ry < N:
                    if visit[rx][ry] == False:
                        visit[rx][ry] = True
                        Q.append((rx,ry))
                        if arr[rx][ry] == 1:
                            res += cnt
                            continue
    return res

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
ch = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            ch.append((i,j))
ans = float('inf')
for com in combinations(ch, M):
    ans = min(ans, bfs(com))
print(ans)