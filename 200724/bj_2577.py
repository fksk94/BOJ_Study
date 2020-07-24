a = int(input())
b = int(input())
c = int(input())

mul_a = a*b*c
list_a = str(mul_a)
list_a = list(list_a)
dic_a = {}


for i in list_a :
    try :
        if dic_a[i] != 0 :
            dic_a[i] += 1
    except :
        dic_a[i] = 1

for i in range(10) :
    try :
        print(dic_a[str(i)])
    except :
        print(0)