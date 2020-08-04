a = [False, False] + [True]*(2*123456 -1)
tmp = []
for i in range(2, 2*123456+1) :
    if a[i]:
        tmp.append(i)
    for j in range(2*i, 2*123456+1, i):
        a[j] = False

while True :
    n = int(input())
    if n == 0 :
        break
    else :
        sum_i = 0
        for num in tmp :
            if n < num <= n*2 :
                sum_i += 1

        print(sum_i)