a = input().split()
b = []
j = 0
for i in a :
    i = list(i)
    i.reverse()
    b.append(i)
    j += 1

if b[0] < b[1] :
    for i in b[1]:
        print(i, end = '')
else :
    for i in b[0] :
        print(i, end = '')