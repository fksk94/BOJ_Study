from sys import stdin, setrecursionlimit
from collections import defaultdict
input = stdin.readline
setrecursionlimit(200000)
import heapq

def find(n):
    while s:
        cost, next, start = heapq.heappop(s)
        if dp[V] < cost:
            return dp[V]
        if dp[next] > dp[start] + cost:
            for i in dic[next]:
                heapq.heappush(s, i)
            dp[next] = dp[start] + cost



V, E, P = map(int, input().split())
dic = defaultdict(list)
for i in range(E):
    a, b, c = list(map(int, input().split()))
    dic[a].append((c, b, a))
    dic[b].append((c, a, b))

s = dic[1][:]

dp = [float('inf')] * (V+1)
dp[1] = 0
heapq.heapify(s)
find(1)

min_len1 = dp[V]
min_len2 = dp[P]

dp = [float('inf')] * (V+1)
dp[P] = 0
s = dic[P][:]
heapq.heapify(s)
find(P)
if min_len2 + dp[V] == min_len1:
    print("SAVE HIM")
else:
    print("GOOD BYE")
