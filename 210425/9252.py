def s():
    s1, s2 = input(), input()
    dp = [0] * 1000
    dp2 = [""] * 1000
    for i in range(len(s1)):
        max_dp = 0
        ch = ""
        for j in range(len(s2)):
            if max_dp < dp[j]:
                max_dp = dp[j]
                ch = dp2[j]
            elif s1[i] == s2[j]:
                dp[j] = max_dp + 1
                dp2[j] = ch + s2[j]
    tmp, idx = 0, 0
    for i in range(1000):
        if tmp < dp[i]:
            tmp = dp[i]
            idx = i
    print(dp[idx])
    print(dp2[idx])
s()