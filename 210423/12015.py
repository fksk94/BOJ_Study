import bisect

N = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]
for j in range(1, N):
    idx= bisect.bisect_left(dp, arr[j])
    if idx == len(dp):
        dp.append(arr[j])
    else:
        dp[idx] = arr[j]

print(len(dp))