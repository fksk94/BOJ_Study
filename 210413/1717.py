from sys import stdin
input = stdin.readline
import sys
sys.setrecursionlimit(200000)

def find(x):
    if x == arr[x]:
        return x
    else:
        arr[x] = find(arr[x])
        return arr[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        arr[y] = x
    else:
        arr[x] = y

N, M = map(int, input().split())
arr = [i for i in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    if a == 0:
        union(b, c)
    else:
        if find(b) == find(c):
            print('YES')
        else:
            print('NO')