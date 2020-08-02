s = list(map(int, input().split()))

s[2] = s[2] - s[0]

if s[2] <= 0 :
    print('1')

elif s[2] == (s[0]-s[1])*(s[2]//(s[0] - s[1])) :
    print(s[2]//(s[0] - s[1])+1)

else :
    print(s[2]//(s[0] - s[1])+2)