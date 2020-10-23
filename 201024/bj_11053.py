N = int(input())
arr = list(map(int, input().split()))
dp = [1] * 1001
for j in range(N):
    for i in range(j, -1, -1):
        if arr[i] < arr[j]:
            dp[j] = max(dp[j], dp[i]+1)

print(max(dp))