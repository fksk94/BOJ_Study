from collections import defaultdict
from sys import stdin
input = stdin.readline
import heapq

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    dic = defaultdict(list)
    for i in range(1, N+1):
        arr =list(map(int, input().split()))
        for j in range(len(arr)):
            dic[(i,j+1)].append((arr[j], (i, j+2)))
            dic[(i, j + 2)].append((arr[j], (i, j + 1)))
    for i in range(1, N):
        arr = list(map(int, input().split()))
        for j in range(len(arr)):
            dic[(i, j+1)].append((arr[j], (i+1, j+1)))
            dic[(i+1, j+1)].append((arr[j], (i, j+1)))
    Q = dic[(1,1)]
    heapq.heapify(Q)
    visit = dict()
    visit[(1,1)] = True
    res = 0
    while Q:
        cost, next = heapq.heappop(Q)
        if visit.get(next):
            continue
        res += cost
        visit[next] = True
        for i in dic[next]:
            heapq.heappush(Q, i)

    print(res)
