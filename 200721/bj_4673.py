b = 0
c = []
while b <= 10000 :
    b += 1
    tmp = int(b + b//1000 + (b%1000 - b%100 + b%10)/100 + b%10 + (b%100 - b%10)/10)
    c.append(tmp)
    for i in c :
        if b == i:
            break
    else :
        print(b)