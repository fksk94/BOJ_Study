import sys
sys.setrecursionlimit(5000)

dx =[0, 0, 1, -1]
dy =[1, -1, 0, 0]

def remove(x, y):
    arr[x][y] = 0
    for i in range(4):
        rx = x + dx[i]
        ry = y + dy[i]
        if -1 < rx < N and -1 < ry < M:
            if arr[rx][ry] == 1:
                remove(rx, ry)

T = int(input())
for _ in range(T):
    N, M, C = map(int, sys.stdin.readline().split())
    arr = [[0]*M for i in range(N)]
    for i in range(C):
        x, y = map(int, sys.stdin.readline().split())
        arr[x][y] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
                remove(i, j)

    print(cnt)
