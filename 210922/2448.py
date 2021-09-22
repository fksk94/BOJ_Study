from sys import stdin
input = stdin.readline

N = int(input())

ans = [[" "] * (N * 2) for i in range(N)]
ans[0][N-1] = "*"

for i in range(N-1):
    for j in range(N*2):
        if ans[i][j] == "*":
            if ans[i][j+1] == "*":
                ch = 2
                break
            if ans[i][j+2] == "*":
                ch = 1
                break
            ch = 0
            break
    if ch == 0:
        j = 0
        while j < N*2:
            if ans[i][j] == "*":
                ans[i+1][j-1] = "*"
                ans[i+1][j+1] = "*"
            j += 1
    if ch == 1:
        j = 0
        while j < N*2:
            if ans[i][j] == "*":
                ans[i+1][j-1] = "*"
                ans[i+1][j] = "*"
                ans[i+1][j+1] = "*"
                ans[i+1][j+2] = "*"
                ans[i+1][j+3] = "*"
                j += 2
            j += 1
    if ch == 2:
        j = 0
        while j < N*2:
            if ans[i][j] == "*":
                ans[i+1][j-1] = "*"
                while True:
                    j += 6
                    if j < N*2 and ans[i][j] == "*":
                        continue
                    break
                ans[i+1][j-1] = "*"
            j += 1

for i in range(N):
    print("".join(ans[i]))
