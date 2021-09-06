from sys import stdin
input = stdin.readline

dxy = [(1, 0), (-1, 0), (0, -1), (0, 1)]


def spread_dust(x, y):
    for dx, dy in dxy:
        rx = x + dx
        ry = y + dy
        if 0 <= rx < N and 0 <= ry < M and room[rx][ry] != -1:
            room2[rx][ry] += room[x][y]//5
            room2[x][y] -= room[x][y]//5


N, M, T = map(int, input().split())
room = [list(map(int, input().split())) for i in range(N)]
room2 = [room[i][:] for i in range(N)]

cleaner = ()

for i in range(N):
    for j in range(M):
        if room[i][j] == -1:
            cleaner = (i, i+1)
            break
    if cleaner:
        break

for _ in range(T):
    for i in range(N):
        for j in range(M):
            if room[i][j] > 0:
                spread_dust(i, j)
    before = room2[cleaner[0]][1]
    room2[cleaner[0]][1] = 0
    for i in range(2, M):
        before, room2[cleaner[0]][i] = room2[cleaner[0]][i], before
    for i in range(cleaner[0]-1, -1, -1):
        before, room2[i][M-1] = room2[i][M-1], before
    for i in range(M-2, -1, -1):
        before, room2[0][i] = room2[0][i], before
    for i in range(1, cleaner[0]):
        before, room2[i][0] = room2[i][0], before

    before = room2[cleaner[1]][1]
    room2[cleaner[1]][1] = 0
    for i in range(2, M):
        before, room2[cleaner[1]][i] = room2[cleaner[1]][i], before
    for i in range(cleaner[1]+1, N):
        before, room2[i][M-1] = room2[i][M-1], before
    for i in range(M-2, -1, -1):
        before, room2[N-1][i] = room2[N-1][i], before
    for i in range(N-2, cleaner[1], -1):
        before, room2[i][0] = room2[i][0], before

    room = [room2[i][:] for i in range(N)]

print(sum([sum(room[i]) for i in range(N)]) + 2)