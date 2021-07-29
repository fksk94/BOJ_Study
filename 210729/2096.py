from sys import stdin
input = stdin.readline

N = int(input())
max_dp = list(map(int, input().split()))
min_dp = max_dp[:]
for i in range(N-1):
    arr = list(map(int, input().split()))
    tmp1 = max_dp[:]
    tmp2 = min_dp[:]
    max_dp[0] = arr[0] + max(tmp1[0], tmp1[1])
    max_dp[1] = arr[1] + max(tmp1[0], tmp1[1], tmp1[2])
    max_dp[2] = arr[2] + max(tmp1[2], tmp1[1])
    min_dp[0] = arr[0] + min(tmp2[0], tmp2[1])
    min_dp[1] = arr[1] + min(tmp2[0], tmp2[1], tmp2[2])
    min_dp[2] = arr[2] + min(tmp2[2], tmp2[1])

print(max(max_dp), min(min_dp))