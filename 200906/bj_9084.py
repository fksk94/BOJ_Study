def solution() :
    a = int(input())
    dp = [1]+ [0] * 100000
    arr = list(map(int, input().split()))
    b = int(input())
    for i in range(a) :
        for j in range(arr[i], b+1) :
            dp[j] += dp[j-arr[i]]
    print(dp[b])
T = int(input())
for i in range(T) :
    solution()