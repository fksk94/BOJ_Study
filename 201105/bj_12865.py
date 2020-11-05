N, K = map(int, input().split())
pre_dp = [0] * (K + 1)
dp = [0] * (K + 1)
for i in range(N):
    W, V = map(int, input().split())
    for j in range(W):
        if K + 1 > j:
            dp[j] = pre_dp[j]
    for j in range(W, K+1):
        dp[j] = max(pre_dp[j-W] + V, pre_dp[j])
    dp, pre_dp = pre_dp, dp
print(max(pre_dp))