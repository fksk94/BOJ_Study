import sys
def solution():
    N, M = map(int, sys.stdin.readline().split())
    arr = [[0]*(N+1)]+ [[0] + list(map(int, sys.stdin.readline().split())) for i in range(N)]
    for j in range(1, N+1):
        for i in range(1, N):
            arr[j][i + 1] = arr[j][i] + arr[j][i + 1]
    for j in range(1, N+1):
        for i in range(1, N):
            arr[i + 1][j] = arr[i][j] + arr[i + 1][j]
    for i in range(M):
        sx, sy, ex, ey = map(int, sys.stdin.readline().split())
        print(arr[ex][ey] + arr[sx-1][sy-1] - arr[ex][sy-1] - arr[sx-1][ey])
solution()