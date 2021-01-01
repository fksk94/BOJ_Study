from sys import stdin
input = stdin.readline

N = int(input())
dp = [1] * N
dp2 = [1] * N
LIS = list(map(int, input().split()))


for j in range(-1, -N-1, -1):
    for i in range(-1, j-1, -1):
        if LIS[i] < LIS[j]:
            dp[j] = max(dp[j], dp[i]+1)

for j in range(N):
    for i in range(j, -1, -1):
        if LIS[i] < LIS[j]:
            dp2[j] = max(dp2[j], dp2[i]+1)
res = 0
for i in range(N):
    if res < dp[i] + dp2[i] - 1:
        res = dp[i] + dp2[i] - 1

print(res)