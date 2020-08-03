num1 = int(input())
num2 = int(input())
sum_num = 0
min_list = [10000]

for num in range(num1, num2+1) :
    if num == 1 :
        continue
    for i in range(2, num2+1) :
        if num == i :
            sum_num += i
            min_list += [i]
            break
        elif not num % i :
            break

if sum_num == 0 :
    print('-1')
else :
    print(sum_num)
if len(min_list) == 1 :
    pass
else : 
    print(min(min_list))