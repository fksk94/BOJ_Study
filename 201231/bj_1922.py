from sys import stdin
from collections import defaultdict
import heapq
input = stdin.readline


N = int(input())
M = int(input())
dic = defaultdict(list)
for i in range(M):
    a, b, c = map(int, input().split())
    dic[a].append((c, b))
    dic[b].append((c, a))

visit = [False] * (N+1)
Q = [(0, 1)]
total = 0
cnt = 0
while Q:
    cost, next = heapq.heappop(Q)
    if visit[next]:
        continue
    for i in range(len(dic[next])):
        heapq.heappush(Q,dic[next][i])
    visit[next] = True
    cnt += 1
    total += cost
    if cnt == N:
        break

print(total)
