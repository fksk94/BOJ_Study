a = int(input())

for i in range(a):
    div_a = 0
    sum_a = 0
    tmp = 0
    b = list(map(int,input().split()))
    div_a = b[0]
    for j in b[1:] :
        sum_a += j
    sum_a = sum_a/div_a
    for j in b[1:] :
        if j > sum_a :
            tmp += 1
    tmp = tmp/div_a*100
    print(f"{tmp:.3f}%")