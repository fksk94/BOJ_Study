import bisect
import heapq

def s():
    N = int(input())
    arr = list(map(int, input().split())) + [100000000000000000]
    res = []
    if arr.count(0) > 1:
        print(0, 0)
    else:
        for i in range(N):
            idx = bisect.bisect_left(arr, -arr[i])
            if arr[idx] == -arr[i]:
                print(arr[i], -arr[i])
                return
            else:
                if idx - 1 != i:
                    heapq.heappush(res, (abs(arr[i] + arr[idx-1]), arr[i], arr[idx-1]))
                if idx != i:
                    heapq.heappush(res, (abs(arr[i] + arr[idx]), arr[i], arr[idx]))
        ans, a, b = heapq.heappop(res)
        if a <= b:
            print(a, b)
        else:
            print(b, a)
s()

