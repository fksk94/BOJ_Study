sum_a = 0
for i in range(5) :
    a = int(input())
    if a < 40 :
        a = 40
    sum_a += a
sum_a = int(sum_a/5)
print(sum_a)