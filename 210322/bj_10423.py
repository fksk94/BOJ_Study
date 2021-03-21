from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

T, M, K = map(int, input().split())
KKK = list(map(int, input().split()))
arr = [list(map(int, input().split())) for i in range(M)]
dic = defaultdict(list)
for i, j, cost in arr:
    dic[i].append((cost, j))
    dic[j].append((cost, i))
Q = []
for n in KKK:
    Q.extend(dic[n][:])
heapq.heapify(Q)
visit = [False] * (T+1)
for n in KKK:
    visit[n] = True
res = 0
size = K
while Q:
    if size == T:
        break
    cost, next = heapq.heappop(Q)
    if visit[next] == False:
        visit[next] = True
        res += cost
        for i in dic[next]:
            heapq.heappush(Q, i)
        size += 1
print(res)