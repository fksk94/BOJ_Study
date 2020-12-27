from sys import stdin
input = stdin.readline

N = int(input())
arr = [tuple(map(int, input().split())) for i in range(N)]
arr.sort()
arr.sort(key=lambda x:x[1])
s = 0
cnt = 0
for i in range(N):
    if s <= arr[i][0]:
        s = arr[i][1]
        cnt += 1
print(cnt)