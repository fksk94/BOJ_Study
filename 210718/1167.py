from collections import defaultdict
from heapq import *
from sys import stdin
input = stdin.readline


N = int(input())
tree = defaultdict(list)

def dfs(s):
    S = tree[s][:]
    res = 0
    nss = 0
    visit[s] = True
    while S:
        nc, ns = S.pop()
        if visit[ns]:
            continue
        visit[ns] = True
        for xc, xs in tree[ns]:
            S.append((xc + nc, xs))
        if res < nc:
            res = nc
            nss = ns
    if s == 1:
        return nss
    else:
        return res

for _ in range(N):
    vertex_info = list(map(int, input().split()))
    for i in range(1, len(vertex_info)-1, 2):
        tree[vertex_info[0]].append((vertex_info[i+1], vertex_info[i]))

visit = [False] * (N+1)
ns = dfs(1)
visit = [False] * (N+1)
print(dfs(ns))