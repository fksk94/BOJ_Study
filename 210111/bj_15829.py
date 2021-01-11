N = int(input())
S = input()
ans = 0
for i in range(N):
    ans += (ord(S[i])-96)*(31**i) % 1234567891
print(ans % 1234567891)