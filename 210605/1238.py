import heapq
from collections import defaultdict
from sys import stdin
#stdin = open('input.txt', 'r')
input = stdin.readline

N, M, X = map(int, input().split())
dic = defaultdict(list)
r_dic = defaultdict(list)
for i in range(M):
    s, e, c = map(int, input().split())
    dic[s].append((c, e))
    r_dic[e].append((c, s))

def djst(dic):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    Q = [(0, X)]
    visit = [False] * (N + 1)
    while Q:
        c, e = heapq.heappop(Q)
        if visit[e]:
            continue
        dp[e] = c
        visit[e] = True
        for nc, ne in dic[e]:
            heapq.heappush(Q, (nc + c, ne))
    return dp

dp1 = djst(dic)
dp2 = djst(r_dic)

print(max([dp1[i] + dp2[i] for i in range(N+1)]))