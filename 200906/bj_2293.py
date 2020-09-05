def solution() :
    a, b = map(int, input().split())
    dp = [1]+ [0] * 100000
    for i in range(a) :
        m = int(input())
        for j in range(m, b+1) :
            dp[j] += dp[j-m]
    print(dp[b])
solution()