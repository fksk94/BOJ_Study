import sys

T = int(input())
arr = [0]*1001
for i in range(T):
    a,b = map(int, sys.stdin.readline().split())
    arr[a] = b

top = max(arr)
loc = arr.index(top)

result = 0
init = 0
for i in range(loc):
    if init < arr[i]:
        init = arr[i]
        result += init
    else:
        result += init
init = 0
for i in range(1000, loc, -1):
    if init < arr[i]:
        init = arr[i]
        result += init
    else:
        result += init

print(result+top)