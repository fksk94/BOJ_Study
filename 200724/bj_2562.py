b = []
for i in range(9) :
    a = int(input())
    b.append(a)
j = 0
max_i = b[0]
max_j = 1
for i in b :
    j += 1
    if i > max_i :
        max_i = i
        max_j = j
    
print(max_i)
print(max_j)