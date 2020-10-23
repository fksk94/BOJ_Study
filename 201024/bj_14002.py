N = int(input())
arr = list(map(int, input().split()))
dp = [1] * 1001
s_arr = [[arr[i]] for i in range(len(arr))]
for j in range(N):
    for i in range(j, -1, -1):
        if arr[i] < arr[j]:
            if dp[j] < dp[i]+1:
                dp[j] = dp[i]+1
                s_arr[j] = s_arr[i][:] + [arr[j]]
a = max(dp)
print(a)
print(*s_arr[dp.index(a)])