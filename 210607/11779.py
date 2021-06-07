import heapq
from collections import defaultdict
from sys import stdin
# stdin = open('input.txt', 'r')
input = stdin.readline


N = int(input())
M = int(input())
dp = [float('inf')] * (N+1)
dic = defaultdict(list)
for i in range(M):
    s, e, c = map(int, input().split())
    dic[s].append((c, e))

v1, v2 = map(int, input().split())

def djst(start, end):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    dp2 = [[] for _ in range(N+1)]
    Q = [(0, start, start)]
    visit = [False] * (N + 1)
    while Q:
        c, e, s = heapq.heappop(Q)
        if visit[e]:
            continue
        dp2[e] = dp2[s] + [e]
        if e == end:
            return [c, dp2[e]]
        dp[e] = c
        visit[e] = True
        for nc, ne in dic[e]:
            heapq.heappush(Q, (nc + c, ne, e))
res = djst(v1, v2)
print(res[0])
print(len(res[1]))
print(*res[1])