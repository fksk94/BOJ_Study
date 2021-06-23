from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(200000)
from collections import defaultdict

def dfs(x):
    if visit[x]:
        return
    visit[x] = True
    for i in dic[x]:
        dfs(i)


N, M = map(int, input().split())
dic = defaultdict(list)
visit = [False] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

cnt = 0
for i in range(1, N+1):
    if visit[i] == False:
        cnt += 1
        dfs(i)

print(cnt)