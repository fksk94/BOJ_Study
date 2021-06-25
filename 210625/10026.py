from sys import stdin
input = stdin.readline


N = int(input())
board = [list(map(int, input().split())) for i in range(N)]
visit = [[False] * N for i in range(N)]

for _ in range(N):
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                for k in range(N):
                    board[i][k] = board[j][k] or board[i][k]
for i in range(N):
    print(*board[i])