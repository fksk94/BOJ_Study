a = int(input())
b = int(input())


s = (a//100)*100
for i in range(100) :
    if (s + i)%b == 0 :
        if i <10 :
            print("0{}".format(i))
        else :
            print(i)
        break