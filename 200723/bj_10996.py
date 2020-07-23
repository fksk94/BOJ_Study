a = int(input())

i, j, z = 0, 1, 0
while z < a :
    while i < a :
        if i != 0:
            print(' ', end='')
        print('*', end='')
        i += 2
    i = 0
    print('')
    while j < a :
        print(' *', end='')
        j += 2
    j = 1
    print('')
    z = z + 1