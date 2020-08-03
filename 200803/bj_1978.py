s = int(input())
nums = list(map(int, input().split()))
sum_num = 0

for num in nums :
    if num == 1 :
        continue
    for i in range(2, 1001) :
        if num == i :
            sum_num += 1
        elif not num % i :
            break
print(sum_num)