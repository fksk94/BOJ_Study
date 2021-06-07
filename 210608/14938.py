import heapq
from collections import defaultdict
from sys import stdin
# stdin = open('input.txt', 'r')
input = stdin.readline


n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
dic = defaultdict(list)
for i in range(r):
    s, e, c = map(int, input().split())
    dic[s].append((c, e))
    dic[e].append((c, s))

def dfs(s):
    Q = [(0, s)]
    res = 0
    visit = [False] * (n + 1)
    while Q:
        c, e = heapq.heappop(Q)
        if visit[e]:
            continue
        visit[e] = True
        res += items[e]
        for nc, ne in dic[e]:
            if nc + c <= m:
                heapq.heappush(Q, (nc + c, ne))

    return res

ans = 0
for i in range(1, n+1):
    ans = max(ans, dfs(i))
print(ans)
