sum_a = 0
com_a = 2000
for i in range(3) :
    a = int(input())
    if com_a > a :
        com_a = a
sum_a += com_a
for i in range(2) :
    a = int(input())
    if com_a > a :
        com_a = a
sum_a += com_a
sum_a = int(sum_a-50)
print(sum_a)