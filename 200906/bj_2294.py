def solution() :
    a, b = map(int, input().split())
    dp = [float('inf')] * 100001
    for i in range(a) :
        m = int(input())
        dp[m] = 1
        for j in range(m+1, b+1) :
            if dp[j] > dp[j-m] + 1 :
                dp[j] = dp[j-m] + 1
    if dp[b] == float('inf') : print(-1)
    else : print(dp[b])
solution()