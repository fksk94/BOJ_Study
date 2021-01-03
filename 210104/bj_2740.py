from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
M, K = map(int, input().split())
B = [list(map(int, input().split())) for i in range(M)]
R = [[0] * K for i in range(N)]

for i in range(N):
    for j in range(K):
        for z in range(M):
            R[i][j] += A[i][z] * B[z][j]

for i in R:
    print(*i)