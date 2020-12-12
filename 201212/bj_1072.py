import sys
sys.setrecursionlimit(100000)

def bns(s, e) :
    if s >= e:
        print(e)
        return
    mid = (s + e) // 2
    if pivot < 100 * (M + mid) // (N + mid):
        bns(s, mid)
    else:
        bns(mid+1, e)

N, M = map(int, input().split())
pivot = 100 * M // N
if N == M:
    print(-1)
elif pivot == 99:
    print(-1)
else:
    bns(1, 1000000000)