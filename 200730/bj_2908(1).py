a = input().split()
b = []
j = 0
x = ''
for i in a :
    i = list(i)
    i.reverse()
    b.append(i)
    j += 1

if b[0] < b[1] :
    x = ''.join(b[1])
    print(x)

else :
    x = ''.join(b[0])
    print(x)
