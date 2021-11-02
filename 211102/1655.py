from sys import stdin
import heapq
input = stdin.readline

T = int(input())
if T == 1:
    print(int(input()))
else:
    arr = [int(input())]
    print(arr[0])
    arr.append(int(input()))
    arr.sort()
    tmp = []
    print(arr[0])
    for i in range(3, T+1):
        n = int(input())
        if len(arr) <= i // 2:
            if arr[0] <= n:
                heapq.heappush(arr, n)
            else:
                heapq.heappush(tmp, -n)
                heapq.heappush(arr, -heapq.heappop(tmp))
        else:
            if arr[0] < n:
                heapq.heappush(arr, n)
                heapq.heappush(tmp, -heapq.heappop(arr))
            else:
                heapq.heappush(tmp, -n)
        print(arr[0])