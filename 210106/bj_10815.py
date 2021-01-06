from sys import stdin
import bisect
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
ch = list(map(int, input().split()))
arr.sort()
for i in ch:
    s = bisect.bisect_left(arr, i)
    if s == N:
        print(0, end=' ')
    elif arr[s] == i:
        print(1, end=' ')
    else:
        print(0, end=' ')