from sys import stdin
import sys
input = stdin.readline
sys.setrecursionlimit(100000)

def check(tmp):
    cnt = 0
    for i in arr:
        if i > tmp:
            cnt += i - tmp
    return cnt

def bs(s, e):
    if s >= e:
        if N <= check(e - 1):
            res.append(e - 1)
        if N <= check(e):
            res.append(e)
        return
    mid = (s+e)//2
    t = check(mid)
    if N == t:
        res.append(mid)
    elif N < t:
        return bs(mid+1, e)
    else:
        return bs(s, mid)

K, N = map(int, input().split())
arr = list(map(int, input().split()))
res = []
bs(0, max(arr))
print(max(res))
