def all_check(n, x, y):
    for z in range(9):
        if board[x][z] == n:
            return False
        if board[z][y] == n:
            return False
        if board[x // 3 * 3 + z // 3][y // 3 * 3 + z % 3] == n:
            return False
    else:
        return True

def dfs(cnt):
    global res
    if len_check == cnt:
        res = board
        return
    ch = check[cnt]
    for i in ch[2]:
        if all_check(i, ch[0], ch[1]):
            board[ch[0]][ch[1]] = i
            dfs(cnt+1)
            if res:
                return
            board[ch[0]][ch[1]] = 0



board = [list(map(int, input().split())) for i in range(9)]
change = True
while change:
    check = []
    change = False
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                tmp = list(range(1,10))
                for z in range(9):
                    if board[i][z] in tmp:
                        tmp.remove(board[i][z])
                    if board[z][j] in tmp:
                        tmp.remove(board[z][j])
                    if board[i//3*3 + z//3][j//3*3 + z%3] in tmp:
                        tmp.remove(board[i//3*3 + z//3][j//3*3 + z%3])
                if len(tmp) == 1:
                    board[i][j] = tmp[0]
                    change = True
                else:
                    check.append((i,j, tmp))

len_check = len(check)
res = []
if check:
    dfs(0)
else:
    res = board

for i in range(81):
    if i%9 == 8:
        print(res[i // 9][i % 9])
    else:
        print(res[i//9][i%9], end =' ')