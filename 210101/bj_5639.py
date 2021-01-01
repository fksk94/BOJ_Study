import sys
import bisect

sys.setrecursionlimit(100000)

def divide(s, e):
    if s >= e:
        return
    mid = s + bisect.bisect_right(arr[s+1:e], arr[s]) + 1
    divide(s+1, mid)
    divide(mid, e)
    print(arr[s])

arr = []
while True:
    try:
        arr.append(int(sys.stdin.readline()))
    except:
        break

divide(0, len(arr))