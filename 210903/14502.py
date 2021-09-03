from itertools import combinations
from sys import stdin
input = stdin.readline

dxy = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def spread_virus(tmp_lab, ni, nj):
    S = [(ni, nj)]
    while S:
        loc_i, loc_j = S.pop()
        for dx, dy in dxy:
            rx = loc_i + dx
            ry = loc_j + dy
            if 0 <= rx < N and 0 <= ry < M and tmp_lab[rx][ry] == 0:
                tmp_lab[rx][ry] = 2
                S.append((rx, ry))

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for i in range(N)]

arr = []
res = 0
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            arr.append((i, j))

for comb in combinations(arr, 3):
    tmp_lab = [lab[i][:] for i in range(N)]
    for i, j in comb:
        tmp_lab[i][j] = 1
    for i in range(N):
        for j in range(M):
            if tmp_lab[i][j] == 2:
                spread_virus(tmp_lab, i, j)

    tmp_res = 0
    for i in range(N):
        tmp_res += tmp_lab[i].count(0)

    res = max(res, tmp_res)

print(res)