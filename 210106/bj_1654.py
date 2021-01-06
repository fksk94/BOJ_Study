from sys import stdin
import sys
input = stdin.readline
sys.setrecursionlimit(100000)

def check(tmp):
    cnt = 0
    if tmp == 0:
        return 1000000000000
    for i in arr:
        cnt += i // tmp
    return cnt

def bs(s, e):
    if s >= e:
        if N <= check(e - 1):
            res.append(e - 1)
        if N <= check(e):
            res.append(e)
        return
    mid = (s+e)//2
    if N == check(mid):
        res.append(mid)
        return bs(mid+1, e)
    elif N < check(mid):
        return bs(mid+1, e)
    else:
        return bs(s, mid)

K, N = map(int, input().split())
arr = [int(input()) for i in range(K)]
res = []
bs(0, max(arr))
print(max(res))
