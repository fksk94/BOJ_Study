# 암호 디코딩

# 암호찾기
def part_dp(pw, e):
    if password[pw] == '0':
        return
    else:
        dp[pw] = 1

    if pw + 1 == e:
        return

    if password[pw+1] == '0':
        dp[pw+1] = 1
    else:
        if password[pw] == '1' or (password[pw] == '2' and int(password[pw+1]) <= 6):
            dp[pw+1] = 2
        else:
            dp[pw+1] = 1
    for i in range(pw+2, e):
        if password[i] == '0':
            dp[i] += dp[i - 2]
        else:
            dp[i] += (dp[i - 1] + dp[i - 2])

# 암호 입력
password = input()

# 암호 나누기
split_pw = [0]
for i in range(len(password)-1):
    if 9 < int(password[i] + password[i+1]) < 27 :
        continue
    else:
        split_pw.append(i+1)
split_pw.append(len(password))


# 암호 찾기
ans = 1
dp = [0] * 5000
for i in range(len(split_pw)-1):
    part_dp(split_pw[i], split_pw[i+1])
    ans *= dp[split_pw[i+1]-1]
if password == '':
    print(0)
else:
    # 와... 1000000으로 안 나눴었네;
    print(ans%1000000)