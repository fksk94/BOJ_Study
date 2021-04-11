from sys import stdin
input = stdin.readline

def find(x):
    if x == island[x]:
        return x
    else:
        island[x] = find(island[x])
        return island[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        island[y] = x
    else:
        island[x] = y

N = int(input())
island = [i for i in range(N+1)]
for i in range(N-2):
    a, b = map(int, input().split())
    union(a, b)

for i in range(1, N):
    if find(i) != find(i+1):
        print(i, i+1)
        break