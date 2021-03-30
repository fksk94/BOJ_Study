from collections import defaultdict
from sys import stdin
input = stdin.readline
import heapq

N, M = map(int, input().split())
arr = [0] + list(input().rstrip().split())
dic = defaultdict(list)
for i in range(M):
    a, b, c = map(int, input().split())
    if arr[a] != arr[b]:
        dic[a].append((c, b))
        dic[b].append((c, a))

Q = dic[1]
heapq.heapify(Q)
visit = [False] * (N+1)
visit[1] = True
res = 0
size = 1
while Q:
    cost, next = heapq.heappop(Q)
    if visit[next]:
        continue
    res += cost
    size += 1
    visit[next] = True
    for i in dic[next]:
        heapq.heappush(Q, i)

if size == N:
    print(res)
else:
    print(-1)