from sys import stdin
import heapq
from collections import defaultdict

V, E = map(int, stdin.readline().split())
weight = ['INF'] * (V + 1)
dic = defaultdict(list)
S = int(stdin.readline())
weight[S] = 0
for _ in range(E):
    u, v, w = map(int, stdin.readline().split())
    dic[u].append((v, w))

q = []
for i, j in dic.get(S):
    heapq.heappush(q, (j, i))

while q:
    we, i = heapq.heappop(q)

    if weight[i] == 'INF':
        weight[i] = we
        while dic.get(i):
            a, b = dic[i].pop()
            heapq.heappush(q, (weight[i] + b, a))

for i in range(1, V+1):
    print(weight[i])