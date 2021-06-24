from sys import stdin
# stdin = open('input.txt', 'r')
input = stdin.readline


N, M = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]

def check(x, y):
    ans = []
    try:
        ans.append(board[x][y] + board[x][y+1] + board[x][y+2] + board[x][y+3])
    except:
        pass

    try:
        ans.append(board[x][y] + board[x+1][y] + board[x+2][y] + board[x+3][y])
    except:
        pass

    try:
        ans.append(board[x][y] + board[x+1][y] + board[x+1][y+1] + board[x][y+1])
    except:
        pass

    # -----
    try:
        ans.append(board[x][y] + board[x + 1][y] + board[x + 2][y] + board[x][y + 1])
    except:
        pass

    try:
        ans.append(board[x][y] + board[x + 1][y] + board[x + 2][y] + board[x][y - 1])
    except:
        pass

    try:
        ans.append(board[x][y] + board[x+1][y] + board[x+2][y] + board[x+2][y+1])
    except:
        pass

    try:
        ans.append(board[x][y] + board[x+1][y] + board[x+2][y] + board[x+2][y-1])
    except:
        pass

    try:
        ans.append(board[x][y] + board[x+1][y] + board[x][y+1] + board[x][y+2])
    except:
        pass

    try:
        ans.append(board[x][y] + board[x+1][y] + board[x][y-1] + board[x][y-2])
    except:
        pass

    try:
        ans.append(board[x][y] + board[x + 1][y] + board[x+1][y + 1] + board[x+1][y + 2])
    except:
        pass

    try:
        ans.append(board[x][y] + board[x + 1][y] + board[x+1][y - 1] + board[x+1][y - 2])
    except:
        pass

    # ---- 2개만 더

    try:
        ans.append(board[x][y] + board[x + 1][y] + board[x + 1][y + 1] + board[x + 2][y + 1])
    except:
        pass

    try:
        ans.append(board[x][y] + board[x + 1][y] + board[x + 1][y - 1] + board[x + 2][y - 1])
    except:
        pass

    try:
        ans.append(board[x][y] + board[x][y + 1] + board[x - 1][y + 1] + board[x - 1][y + 2])
    except:
        pass

    try:
        ans.append(board[x][y] + board[x][y - 1] + board[x - 1][y - 1] + board[x - 1][y - 2])
    except:
        pass

    # --- 마지막

    try:
        ans.append(board[x][y] + board[x][y + 1] + board[x][y + 2] + board[x + 1][y + 1])
    except:
        pass

    try:
        ans.append(board[x][y] + board[x][y + 1] + board[x][y + 2] + board[x - 1][y + 1])
    except:
        pass

    try:
        ans.append(board[x][y] + board[x + 1][y] + board[x + 2][y] + board[x + 1][y + 1])
    except:
        pass

    try:
        ans.append(board[x][y] + board[x + 1][y] + board[x + 2][y] + board[x + 1][y - 1])
    except:
        pass

    if ans:
        return max(ans)
    return 0

ans = []
for i in range(N):
    for j in range(M):
        ans.append(check(i, j))

print(max(ans))