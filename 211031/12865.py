N, K = map(int, input().split())

dp = [0] * (K+1)
dp2 = [0] * (K+1)
for _ in range(N):
    a, b = map(int, input().split())
    for i in range(1, K+1):
        if i-a > -1:
            dp2[i] = max(dp[i], dp[i-a] + b)
    dp = dp2[:]
print(max(dp))