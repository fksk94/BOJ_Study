from collections import defaultdict
from heapq import *
from sys import stdin
input = stdin.readline


N = int(input())
M = int(input())
ans = [[float("inf")] * N for _ in range(N)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    ans[start-1][end-1] = min(ans[start-1][end-1], cost)

for _ in range(N):
    ans[_][_] = 0

for i in range(N):
    for j in range(N):
        for k in range(N):
            ans[j][k] = min(ans[j][i] + ans[i][k], ans[j][k])

for i in range(N):
    for j in range(N):
        if ans[i][j] == float('inf'):
            ans[i][j] = 0

for i in range(N):
    print(*ans[i])