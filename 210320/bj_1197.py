from collections import defaultdict
from sys import stdin
input = stdin.readline
import heapq

gems = []
N, K = map(int, input().split())
dic = defaultdict(list)
for i in range(K):
    v, w, c = map(int, input().split())
    dic[v].append((c, w))
    dic[w].append((c, v))

Q = dic[1][:]
visit = [False] * (N+1)
visit[1] = True
res = 0
heapq.heapify(Q)
size = 1
while Q:
    if size == N:
        break
    cost, next = heapq.heappop(Q)
    if visit[next]:
        continue
    res += cost
    for j in dic[next]:
        heapq.heappush(Q, j)
    visit[next] = True
    size += 1

print(res)