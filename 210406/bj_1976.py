from sys import stdin
input = stdin.readline

def find(x):
    if x == cities[x]:
        return x
    else:
        cities[x] = find(cities[x])
        return cities[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        cities[y] = x
    else:
        cities[x] = y

N = int(input())
M = int(input())
cities = [i for i in range(201)]
for i in range(1, N+1):
    arr = list(map(int, input().split()))
    for j in range(i, N+1):
        if arr[j-1]:
            union(i, j)

tmp = list(map(int, input().split()))
x = find(tmp[0])
for j in tmp:
    if find(j) != x:
        print('NO')
        break
else:
    print('YES')