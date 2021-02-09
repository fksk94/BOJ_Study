from sys import stdin
input = stdin.readline


N = int(input())
arr = [0] + [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)

for i in range(1, N+1):
    if len(arr[i]) == 2:
        dp[i] = arr[i][0]

for i in range(1, N+1):
    for j in range(1, N+1):
        for z in range(1, len(arr[j])-1):
            dp[j] = max(dp[j], dp[arr[j][z]]+ arr[j][0])

for i in range(1, N+1):
    print(dp[i])