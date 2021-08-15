from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

dxy = [(1,0), (0,1), (-1,0), (0, -1)]


def outer(r, c, cnt):
    board[r][c] = -cnt
    for i in range(4):
        nr = r + dxy[i][0]
        nc = c + dxy[i][1]
        if 0 <= nr < R and 0 <= nc < C and -cnt < board[nr][nc] < 1 :
            outer(nr, nc, cnt)


cnt = 1
ans = 0

while True:
    for ci in range(C):
        if board[0][ci] == -cnt+1:
            outer(0, ci, cnt)
        if board[R-1][ci] == -cnt+1:
            outer(R-1, ci, cnt)

    for ri in range(1, R-1):
        if board[ri][0] == -cnt+1:
            outer(ri, 0, cnt)
        if board[ri][C-1] == -cnt+1:
            outer(ri, C-1, cnt)

    arr = []
    for i in range(R):
        for j in range(C):
            if board[i][j] == 1:
                tmp = 0
                for k in range(4):
                    ni = i + dxy[k][0]
                    nj = j + dxy[k][1]
                    if 0 <= ni < R and 0 <= nj < C and board[ni][nj] == -cnt:
                        tmp += 1
                if tmp > 1:
                    arr.append((i, j))

    if arr:
        for i, j in arr:
            board[i][j] = -cnt
        ans += 1
        cnt += 1
    else:
        break

print(ans)