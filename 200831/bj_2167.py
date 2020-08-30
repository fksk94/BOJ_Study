import sys

n, m = map(int, input().split())
arr = []
for i in range(n) :
    arr.append(list(map(int, sys.stdin.readline().split())))

arr_sum = [[] for _ in range(n)]
for j in range(n) :
    for i in range(m) :
        arr_sum[j].append(sum(arr[j][:i+1]))

for i in range(m):
    for j in range(1, n):
        arr_sum[j][i] += arr_sum[j-1][i]

k = int(input())
for i in range(k) :
    i, j, x, y = map(int, sys.stdin.readline().split())
    if i == x and j == y :
        result = arr[i-1][j-1]
    elif i == 1 and j == 1:
        result = arr_sum[x - 1][y - 1]
    elif i == 1 :
        result = arr_sum[x - 1][y - 1] - arr_sum[x-1][j-2]
    elif j == 1 :
        result = arr_sum[x - 1][y - 1] - arr_sum[i - 2][y - 1]
    else :
        result = arr_sum[x-1][y-1] - arr_sum[i-2][y-1] - arr_sum[x-1][j-2] + arr_sum[i-2][j-2]
    print(result)