from collections import deque
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
arr = [input().rstrip() for i in range(N)]
visit = [[False] * M for i in range(N)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(x, y):
    Q = deque([(x, y)])
    cnt = 0
    while Q:
        cnt += 1
        for _ in range(len(Q)):
            n, m = Q.popleft()
            if n == N-1 and m == M-1:
                return cnt
            for i in range(4):
                rn = n + dxy[i][1]
                rm = m + dxy[i][0]
                if 0 <= rm < M and 0 <= rn < N and visit[rn][rm] == False and arr[rn][rm] == '1':
                    Q.append((rn, rm))
                    visit[rn][rm] = True
    return cnt

print(bfs(0, 0))