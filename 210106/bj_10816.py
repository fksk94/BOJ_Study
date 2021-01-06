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
    e = bisect.bisect_right(arr, i)
    print(e-s, end=' ')