from collections import deque
import sys

visited = []
res = 0

def solution():
    global res, visited

    def bfs(x, y, n):
        global res, visited
        Q = deque([(x, y)])
        tmp = [(x,y)]
        sig = True
        visited[x][y] = 1
        cnt = 1
        while True:
            x, y = Q.popleft()
            for _ in range(4):
                rx = x + dx[_]
                ry = y + dy[_]
                if rx == -1 or rx == N or ry == -1 or ry == M:
                    sig = False
                    continue
                if board[rx][ry] <= n and visited[rx][ry] == 0:
                    visited[rx][ry] = 1
                    Q.append((rx, ry))
                    cnt += 1
            if not Q:
                if sig:
                    res += cnt
                return


    N, M = map(int, input().split())
    board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    for num in range(1, 9):
        visited = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if board[i][j] <= num and visited[i][j] == 0:
                    bfs(i, j, num)
    print(res)
solution()