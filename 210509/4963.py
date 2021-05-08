from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(3000)

def dfs(x, y):
    visit[x][y] = True
    for dx, dy in dxy:
        rx, ry = dx + x, dy + y
        if 0 <= rx < M and 0 <= ry < N:
            if virtual_map[rx][ry] == 1 and visit[rx][ry] == False:
                dfs(rx, ry)
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    virtual_map = [list(map(int, input().split())) for _ in range(M)]
    visit = [[False] * N for _ in range(M)]
    dxy = [(0, -1), (0, 1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    cnt = 0

    for i in range(M):
        for j in range(N):
            if virtual_map[i][j] == 1 and visit[i][j] == False:
                dfs(i, j)
                cnt += 1

    print(cnt)