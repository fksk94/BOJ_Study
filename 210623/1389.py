from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(200000)
from collections import defaultdict, deque

def bfs(x, cnt):
    global res
    Q = deque(dic[x][:])
    visit[x] = True
    while Q:
        cnt += 1
        for _ in range(len(Q)):
            x = Q.popleft()
            if visit[x]:
                continue
            res += cnt
            visit[x] = True
            for i in dic[x]:
                Q.append(i)


N, M = map(int, input().split())
dic = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

ans = []
for i in range(N, 0, -1):
    visit = [False] * (N + 1)
    res = 0
    bfs(i, 0)
    ans.append((res, i))

ans.sort()
print(ans[0][1])