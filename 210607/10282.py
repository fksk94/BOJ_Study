import heapq
from collections import defaultdict
from sys import stdin
# stdin = open('input.txt', 'r')
input = stdin.readline


T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    dp = [float('inf')] * (N+1)
    dic = defaultdict(list)
    for i in range(M):
        s, e, c = map(int, input().split())
        dic[e].append((c, s))

    def djst(start):
        dp = [float('inf')] * (N + 1)
        dp[0] = 0
        Q = [(0, start)]
        visit = [False] * (N + 1)
        while Q:
            c, e = heapq.heappop(Q)
            if visit[e]:
                continue
            dp[e] = c
            visit[e] = True
            for nc, ne in dic[e]:
                heapq.heappush(Q, (nc + c, ne))
        return [sum(visit), max([_ if _ != float('inf') else 0 for _ in dp])]

    print(*djst(C))
