from collections import deque
from sys import stdin
input = stdin.readline


T = int(input())

def bfs():
    Q = deque([start])
    cnt = 0
    while Q:
        for ci in range(len(Q)):
            nextLocation = Q.popleft()
            if nextLocation == end:
                return cnt
            if visit[nextLocation[0]][nextLocation[1]]:
                visit[nextLocation[0]][nextLocation[1]] = False
                for i in range(8):
                    nx = nextLocation[0] + direction[i][0]
                    ny = nextLocation[1] + direction[i][1]
                    if 0 <= nx < N and 0 <= ny < N and visit[nx][ny]:
                        Q.append((nx, ny))
        cnt += 1

for _ in range(T):
    N = int(input())
    visit = [[True] * N for i in range(N)]
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    direction = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]
    print(bfs())