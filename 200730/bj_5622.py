s = input()
sum_i = 0

for i in s :
    if ord(i) >= 87 :
        sum_i += 10
    elif ord(i) == 86 :
        sum_i += 9
    elif ord(i) == 83 :
        sum_i += 8
    else :
        sum_i += (ord(i)-56)//3
    
print(sum_i)