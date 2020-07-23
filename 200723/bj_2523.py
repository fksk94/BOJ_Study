a = int(input())

i, z = 0, 0

while i < a :
    i += 1
    j = a - i
    while j < a :
        j += 1
        print("*", end='')
    print('')
    if i == a :
        z = i - 1
        while 0 < z < a :
            print('*'* z)
            z -= 1