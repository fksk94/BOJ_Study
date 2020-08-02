s = int(input())

for i in range(s):
    a = list(map(int, input().split()))
    meter = a[1] - a[0]
    n1, n2 = 0, 1
    comp = 0
    j = 0
    while True :
        j += 1
        if j%2 :
            comp += n2
            n1 += 1
        else :
            comp += n1
            n2 += 1
        if meter <= comp :
            print(j)
            break