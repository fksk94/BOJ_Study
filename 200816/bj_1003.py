def fibo(n) :
    dp = [0, 0]
    if dp_0[n] > 0 or dp_1[n] >0 :
        return [dp_0[n], dp_1[n]]
    else :
        dp[0] = fibo(n-1)[0] + fibo(n-2)[0]
        dp[1] = fibo(n-1)[1] + fibo(n-2)[1]
        dp_0[n] = dp[0]
        dp_1[n] = dp[1]
        return dp

s = int(input())
for i in range(s) :
    dp_0 = [1, 0] + [0] * 39
    dp_1 = [0, 1] + [0] * 39
    n = int(input())
    fibo(n)
    print('{} {}'.format(dp_0[n], dp_1[n]))