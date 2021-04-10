from sys import stdin
input = stdin.readline

def find(x):
    if x == parties[x]:
        return x
    else:
        parties[x] = find(parties[x])
        return parties[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parties[y] = x
    else:
        parties[x] = y

N, M = map(int, input().split())
trues = list(map(int, input().split()))
rtrues = []
parties = [i for i in range(N+1)]
aarr = [list(map(int, input().split())) for i in range(M)]
for arr in aarr:
    for j in range(1, arr[0]):
        union(arr[j], arr[j+1])
for i in range(1, trues[0]+1):
    rtrues.append(find(trues[i]))

cnt = 0
for arr in aarr:
    if not find(arr[1]) in rtrues:
        cnt += 1

print(cnt)