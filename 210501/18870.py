from sys import stdin
input = stdin.readline

n = int(input())
arr = list(enumerate(map(int, input().split())))
res = [0] * n
arr.sort(key=lambda x:x[1])
j = 0
before = arr[0][1]
res[arr[0][0]] = 0
for i in range(1, len(arr)):
    if before == arr[i][1]:
        res[arr[i][0]] = j
        continue
    j += 1
    res[arr[i][0]] = j
    before = arr[i][1]
print(*res)