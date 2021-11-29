from sys import stdin
from collections import defaultdict
input = stdin.readline

def dfs(s, c):
    if s == b:
        ans.append(c)
        return
    for i in dic[s]:
        if visit.get(i[1]):
            continue
        visit[i[1]] = True
        dfs(i[1], c + i[0])


N, M = map(int, input().split())
dic = defaultdict(list)
ans = []

for i in range(N-1):
    a, b, c = map(int, input().split())
    dic[a].append((c, b))
    dic[b].append((c, a))

for i in range(M):
    visit = dict()
    a, b = map(int, input().split())
    visit[a] = True
    dfs(a, 0)
for i in ans:
    print(i)