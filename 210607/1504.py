import heapq
from collections import defaultdict
from sys import stdin
# stdin = open('input.txt', 'r')
input = stdin.readline


N, M = map(int, input().split())
dp = [float('inf')] * (N+1)
dic = defaultdict(list)
for i in range(M):
    s, e, c = map(int, input().split())
    dic[s].append((c, e))
    dic[e].append((c, s))

v1, v2 = map(int, input().split())

def djst(start, end):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    Q = [(0, start)]
    visit = [False] * (N + 1)
    while Q:
        c, e = heapq.heappop(Q)
        if e == end:
            return c
        if visit[e]:
            continue
        dp[e] = c
        visit[e] = True
        for nc, ne in dic[e]:
            heapq.heappush(Q, (nc + c, ne))
try:
    print(min(djst(1, v1) + djst(N, v2), djst(N, v1) + djst(1, v2)) + djst(v1, v2))
except:
    print(-1)