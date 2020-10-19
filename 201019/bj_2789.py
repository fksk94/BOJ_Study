a = input()
for i in range(len(a)):
    if not a[i] in list('CAMBRIDGE'):
        print(a[i], end='')
