a = int(input())

for i in range(a) :
    tmp_a = 0
    sum_a = 0
    b = list(input())
    for j in b :
        if j == 'X' :
            tmp_a = 0
        elif j == 'O' :
            tmp_a += 1
            sum_a += tmp_a
    print(sum_a)