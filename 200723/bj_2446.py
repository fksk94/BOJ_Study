a = int(input())

i, j = 0, (-a) + 1
b = a
while i < 2*a-1 :
    i += 1
    while -a < j < a :
        if j > abs(b-1) :
            print("", end='')
        elif abs(j) > abs(b-1) :
            print(" ", end='')
        else :
            print("*", end='')
        j += 1
    b -= 1
    j = (-a) + 1
    if a != -b :
        print('')