import heapq
from collections import defaultdict
from sys import stdin
input = stdin.readline


N = int(input())
M = int(input())
dic = defaultdict(list)
for _ in range(M):
    a, b, c =map(int, input().split())
    dic[a].append((c,b))

s, e = map(int, input().split())
Q = [(0,s)]
dp = [float('inf')] * (N+1)
dp[s] = 0
while Q:
    tmp = heapq.heappop(Q)
    for i in dic[tmp[1]]:
        if dp[i[1]] > dp[tmp[1]] + i[0]:
            dp[i[1]] = dp[tmp[1]] + i[0]
            heapq.heappush(Q, i)

print(dp[e])