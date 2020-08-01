s = list(map(int, input().split()))

n = 0

if s[2] > s[1] :
    n = s[0] // (s[2] - s[1]) +1
    print(n)

else :
    print('-1')