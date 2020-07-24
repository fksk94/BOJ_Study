b = []
for i in range(10) :
    a = int(input())
    b.append(a%42)
    
dic_a = {}

for i in b :
    try :
        if dic_a[i] != 0 :
            dic_a[i] += 1
    except :
        dic_a[i] = 1

print(len(dic_a))