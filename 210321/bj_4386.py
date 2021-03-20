from collections import defaultdict
import heapq

T = int(input())
arr = [list(map(float, input().split())) for i in range(T)]
dic = defaultdict(list)
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        cost = ((arr[i][0] - arr[j][0])**2 + (arr[i][1] - arr[j][1])**2)**(1/2)
        dic[i].append((cost, j))
        dic[j].append((cost, i))

Q = dic[0][:]
heapq.heapify(Q)
visit = [False] * T
visit[0] = True
res = 0
size = 1
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
print("{:.2f}".format(res))