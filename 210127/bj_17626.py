N = int(input())
dp = [float('inf')] * 50001
dp[0] = 0
for j in range(1, 50001):
    dp[j] = min([dp[j-(m**2)]+1 for m in range(1, int(j**0.5)+1)])
print(dp[N])