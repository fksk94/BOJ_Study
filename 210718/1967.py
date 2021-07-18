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

for _ in range(N-1):
    a, b, c = map(int, input().split())
    tree[a].append((c, b))
    tree[b].append((c, a))

visit = [False] * (N+1)
ns = dfs(1)
visit = [False] * (N+1)
print(dfs(ns))