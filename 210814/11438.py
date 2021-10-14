from collections import defaultdict, deque
from sys import stdin
import math
input = stdin.readline

N = int(input())
dic = [[] for _ in range(N + 1)]
logN = math.ceil(math.log2(N))
for i in range(N-1):
    n, m = map(int, input().split())
    dic[n].append(m)
    dic[m].append(n)

hierarchy = [0] * (N+1)
parents = [[0] * logN for i in range(N+1)]
hierarchy[1] = 1

Q = deque([1])
while Q:
    node = Q.popleft()
    for i in dic[node]:
        if not hierarchy[i]:
            Q.append(i)
            parents[i][0] = node
            hierarchy[i]=hierarchy[node]+1

for i in range(1, logN):
    for j in range(1, N + 1):
        parents[j][i] = parents[parents[j][i-1]][i-1]


M = int(input())
for _ in range(M):
    n, m = map(int, input().split())
    if hierarchy[n] > hierarchy[m]:
        n, m = m, n

    diff = hierarchy[m] - hierarchy[n]

    for i in range(logN):
        if diff & 1<<i:
            m = parents[m][i]

    if n == m:
        print(n)
        continue

    for i in range(logN - 1, -1, -1):
        if parents[m][i] != parents[n][i]:
            n = parents[n][i]
            m = parents[m][i]

    print(parents[n][0])