import heapq
from collections import defaultdict
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
dic = defaultdict(list)
for i in range(M):
    a, b, c = map(int, input().split())
    dic[a].append((c,b))
    dic[b].append((c,a))

cnt = []
Q = dic[1]
visit = [True] * 100001
visit[1] = False
heapq.heapify(Q)
while Q:
    cost, next = heapq.heappop(Q)
    if visit[next]:
        visit[next] = False
        cnt.append(cost)
        for i in dic[next]:
            if visit[i[1]]:
                heapq.heappush(Q, i)

    if len(cnt) == N-1:
        break

print(sum(cnt) - max(cnt))
