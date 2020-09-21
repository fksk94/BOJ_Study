import sys

def des_bfs(xy, des, cnt):
    global F, sig
    if (xy[0], xy[1]) == des:
        real_Q.append(xy)
        F += cnt*2
        sig = False
        return

    for i in range(4):
        x = xy[0] + dx[i]
        y = xy[1] + dy[i]
        if -1 < x < N and -1 < y < N and board[x][y] != 1 and visited[x][y] == 0:
            visited[x][y] = 1
            Q.append((x,y))

def bfs(xy):
    global F, sig, des
    if 1 < board[xy[0]][xy[1]]:
        des = destination[board[xy[0]][xy[1]]]
        real_Q.append((xy, des))
        sig = True
        return

    for i in range(4):
        x = xy[0] + dx[i]
        y = xy[1] + dy[i]
        if -1 < x < N and -1 < y < N and board[x][y] != 1 and visited[x][y] == 0:
            visited[x][y] = 1
            Q.append((x,y))

N, C, F = map(int, input().split())
board = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
visited = [[0]*N for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
start = tuple(map(int, input().split()))
destination = [0, 0]

for i in range(2,C+2):
    a, b, c, d = map(int, sys.stdin.readline().split())
    board[a-1][b-1] = i
    destination.append((c-1,d-1))

Q = [(start[0]-1, start[1]-1)]
sig = False
des = 0
End = C
while Q:
    if F < 0:
        print(F)
        break
    if End == 0:
        print(F)
        break
    real_Q = []
    if not sig:
        cnt = 0
        for i in range(len(Q)):
            bfs(Q.pop(0))
        if sig:
            real_Q.sort()
            Q = [real_Q[0][0]]
            des = real_Q[0][1]
            board[Q[0][0]][Q[0][1]] = 0
            visited = [[0] * N for _ in range(N)]
        if not sig:
            F -= 1

    if sig:
        for i in range(len(Q)):
            des_bfs(Q.pop(0), des, cnt)
            if not sig:
                Q = [real_Q[0]]
                End -= 1
                F += 1
                visited = [[0] * N for _ in range(N)]
                break
        F -= 1
        cnt += 1
else:
    print(-1)