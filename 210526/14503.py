from sys import stdin
input = stdin.readline

# 입력
n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for i in range(n)]
visit = [[False] * m for i in range(n)]


# 방향 한칸 전진
def direction(x, y, d):
    # 북쪽
    if d == 0:
        return (x - 1, y)
    # 동쪽
    elif d == 1:
        return (x, y + 1)
    # 남쪽
    elif d == 2:
        return (x + 1, y)
    # 서쪽
    return (x, y - 1)


# 탐색
res = 1
visit[r][c] = True
while True:
    for i in range(4):
        d = (d - 1) % 4
        rr, rc = direction(r, c, d)
        if board[rr][rc] == 1 or visit[rr][rc]:
            continue
        r, c = rr, rc
        visit[rr][rc] = True
        res += 1
        break
    else:
        r, c = direction(r, c, (d - 2) % 4)
        if board[r][c] == 1:
            break
print(res)
