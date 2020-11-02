import sys, bisect

N = int(input())
arr = [0] + list(map(int, sys.stdin.readline().split()))

k = 0
result = [arr[1]]
for i in range(2, N+1):
    if result[k] < arr[i]:
        k += 1
        result.append(arr[i])
    else:
        result[bisect.bisect_left(result, arr[i])] = arr[i]
print(N-k-1)