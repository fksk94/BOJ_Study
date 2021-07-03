from collections import deque
from sys import stdin
input = stdin.readline

M, N, H = map(int, input().split())
arr = []
for i in range(H):
    arr.append([])
    for j in range(N):
        arr[i].append(list(map(int, input().split())))

dxy = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]

Q = deque([])
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                Q.append((i, j, k))
cnt = 0
while Q:
    for _ in range(len(Q)):
        h, n, m = Q.popleft()
        for i in range(6):
            rm = m + dxy[i][0]
            rn = n + dxy[i][1]
            rh = h + dxy[i][2]
            if 0 <= rh < H and 0 <= rm < M and 0 <= rn < N and arr[rh][rn][rm] == 0:
                Q.append((rh, rn, rm))
                arr[rh][rn][rm] = 1
    if Q:
        cnt += 1

def ans():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 0:
                    return -1
    return cnt
print(ans())