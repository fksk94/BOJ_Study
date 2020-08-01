s = int(input())
total = 0
i = 0
sum_i = 0

while i < s :
    if (s-i)%5 == 0 :
        total = (s-i)//5 + sum_i
        break
    i += 3
    sum_i += 1

if i == s :
    print(sum_i)
elif i < s :
    print(total)
else :
    print(-1)