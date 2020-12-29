from sys import stdin
input = stdin.readline

N = int(input())
dp = [0] * 501
tmp_dp = [0] * 501
for _ in range(N):
    arr = list(map(int, input().split()))
    for j in range(len(arr)):
        tmp_dp[j] = max(dp[j], dp[j] + arr[j], dp[j-1] + arr[j])
    dp = tmp_dp[:]
print(max(dp))