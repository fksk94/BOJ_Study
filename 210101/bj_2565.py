from sys import stdin
input = stdin.readline

N = int(input())
dp = [0] * 501
LIS = [0] * 501
for i in range(N):
    a,b = map(int, input().split())
    LIS[b] = a
    dp[b] = 1

for j in range(501):
    if LIS[j] == 0:
        continue
    for i in range(j, -1, -1):
        if LIS[i] < LIS[j]:
            dp[j] = max(dp[j], dp[i]+1)

print(N - max(dp))