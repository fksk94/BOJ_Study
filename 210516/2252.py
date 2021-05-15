from collections import defaultdict
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
S = []
arr = [0] * (N+1)
dic = defaultdict(list)

for i in range(M):
    a, b = map(int, input().split())
    dic[a].append(b)
    arr[b] += 1

for i in range(1, N+1):
    if arr[i] == 0:
        S.append(i)

while S:
    to = S.pop()
    print(to, end=" ")
    for i in dic[to]:
        arr[i] -= 1
        if arr[i] == 0:
            S.append(i)