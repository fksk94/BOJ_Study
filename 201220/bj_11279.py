import heapq, sys

N = int(input())
arr = []
for i in range(N):
    a = -int(sys.stdin.readline())
    if a == 0:
        if arr:
            print(-heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, a)