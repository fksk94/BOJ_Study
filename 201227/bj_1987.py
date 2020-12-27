from sys import stdin
input = stdin.readline

def dfs(x, y, cnt):
    global res
    if res == 26:
        return
    if res < cnt:
        res = cnt
    for i in range(4):
        rx = x + dxy[i][0]
        ry = y + dxy[i][1]
        if 0 <= rx < R and 0 <= ry < C and check[ord(board[rx][ry])]:
            check[ord(board[rx][ry])] = False
            dfs(rx, ry, cnt+1)
            check[ord(board[rx][ry])] = True


R, C = map(int, input().split())
board = [input().rstrip() for i in range(R)]
check = [True] * 100
check[ord(board[0][0])] = False
res = 1
dxy = [(-1,0), (1,0), (0,-1), (0,1)]
dfs(0, 0, 1)
print(res)