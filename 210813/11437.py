from collections import defaultdict
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(2000000)

dic = defaultdict(list)

N = int(input())
for i in range(N-1):
    n, m = map(int, input().split())
    dic[n].append(m)
    dic[m].append(n)

hierarchy = [0] * (N+1)
parents = [0 for i in range(N+1)]
hierarchy[1] = 1

def dfs(parent, cnt):
    for p in dic[parent]:
        if hierarchy[p] == 0:
            parents[p] = parent
            hierarchy[p] = cnt
            dfs(p, cnt+1)

dfs(1, 2)

mem = dict()
M = int(input())
for _ in range(M):
    n, m = map(int, input().split())
    if hierarchy[n] > hierarchy[m]:
        n, m = m, n
    arr = set()

    if mem.get((n, m)):
        print(mem.get((n, m)))
        continue
    arr.add((n, m))

    while hierarchy[m] != hierarchy[n]:
        m = parents[m]
        arr.add((n, m))

    while n != m:
        n, m = parents[n], parents[m]
    for i in arr:
        mem[i] = n
    print(n)