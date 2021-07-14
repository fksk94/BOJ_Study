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
while Q:
    tmp = heapq.heappop(Q)
    if dp[tmp[1]] == float('inf'):
        dp[tmp[1]] = tmp[0]
    else:
        continue
    for i in dic[tmp[1]]:
        heapq.heappush(Q, (tmp[0] + i[0], i[1]))

print(dp[e])