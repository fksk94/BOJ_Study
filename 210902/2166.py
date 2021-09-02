from sys import stdin
input = stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
res1, res2 = 0, 0
for i in range(N):
    res1 += arr[i][0] * arr[i - 1][1]
    res2 += arr[i][1] * arr[i - 1][0]

print(round(abs(res1 - res2)/2, 1))