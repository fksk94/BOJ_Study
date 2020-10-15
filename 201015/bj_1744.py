import sys
from collections import deque

T = int(input())
arr = []
for _ in range(T):
    arr.append(int(sys.stdin.readline()))
arr.sort()
res = 0
while len(arr) > 1:
    a = arr.pop()
    b = arr.pop()
    if a > 1 and b > 1 :
        res += a*b
    elif a > 1:
        res += a
        arr.append(b)
        break
    else:
        arr.append(b)
        arr.append(a)
        break
arr = deque(arr)
while len(arr) > 1:
    a = arr.popleft()
    b = arr.popleft()
    if a < 1 and b < 1 :
        res += a*b
    elif a < 1:
        res += a
        res += b
        break
    else:
        res += a
        res += b
        break
for i in arr:
    res += i

print(res)