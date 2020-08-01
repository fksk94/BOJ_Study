s = int(input())

i = 1
sum_i = 1

while i < s :
    i = i + 6*sum_i
    sum_i += 1
    
print(sum_i)