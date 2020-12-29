from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
Q = deque([N])

arr = [False] * (10**6+1)
arr[N] = 1

while Q:
    tmp = Q.popleft()
    if tmp % 3 == 0 and arr[tmp//3] == False:
        arr[tmp//3] = arr[tmp] + 1
        Q.append(tmp//3)
    if tmp % 2 == 0 and arr[tmp//2] == False:
        arr[tmp//2] = arr[tmp] + 1
        Q.append(tmp//2)
    if arr[tmp-1] == False:
        arr[tmp-1] = arr[tmp] + 1
        Q.append(tmp-1)
    if arr[1]:
        break
print(arr[1]-1)
