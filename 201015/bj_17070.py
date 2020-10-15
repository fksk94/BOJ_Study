def dfs(scale):
    for j in range(scale-1):
        for k in range(3):
            if dp[j][scale-2][k]:
                s = (j, scale-2, k)
                for i in range(3):
                    if s[2] - 1 <= i <= s[2] + 1:
                        rx = s[0] + dx[i]
                        ry = s[1] + dy[i]
                        if rx == scale or ry == scale:
                            continue
                        if board[rx][ry] == 1:
                            continue
                        if i == 1:
                            if board[rx-1][ry] == 1 or board[rx][ry-1] == 1 or board[rx-1][ry-1] == 1:
                                continue
                        if rx == scale-1 or ry == scale-1:
                            dp[rx][ry][i] += dp[j][scale-2][k]
    for j in range(2, scale-2):
        for k in range(3):
            if dp[scale-2][j][k]:
                s = (scale-2, j, k)
                for i in range(3):
                    if s[2] - 1 <= i <= s[2] + 1:
                        rx = s[0] + dx[i]
                        ry = s[1] + dy[i]
                        if rx == scale or ry == scale:
                            continue
                        if board[rx][ry] == 1:
                            continue
                        if i == 1:
                            if board[rx-1][ry] == 1 or board[rx][ry-1] == 1 or board[rx-1][ry-1] == 1:
                                continue
                        if rx == scale-1 or ry == scale-1:
                            dp[rx][ry][i] += dp[scale-2][j][k]
    for i in range(scale-1):
        if board[i+1][scale - 1] == 0:
            dp[i+1][scale - 1][0] += dp[i][scale - 1][1]
            dp[i+1][scale - 1][0] += dp[i][scale - 1][0]
        if board[scale - 1][i+1] == 0:
            dp[scale - 1][i+1][2] += dp[scale - 1][i][1]
            dp[scale - 1][i+1][2] += dp[scale - 1][i][2]

# 입력
N = int(input())
board = [list(map(int, input().split())) for i in range(N)]

# 초기값 설정
if board[N-1][N-1]:
    print(0)
else:
    dx = [1, 1, 0]
    dy = [0, 1, 1]
    dp = [[[0]*3 for i in range(N)] for j in range(N)]
    dp[0][1][2] = 1
    start = (0, 1, 2)
    for i in range(3, N + 1):
        dfs(i)
    print(sum(dp[N-1][N-1]))