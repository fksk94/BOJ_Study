a, b, c = map(int, input().split())
max_i = a
tmp = 0
if b < c :
    tmp = b
    b = c
    c = tmp
    if a < b :
        tmp = a
        a = b
        b = tmp
        if b < c :
            tmp = b
            b = c
            c = tmp
else :
    if a < b :
        tmp = a
        a = b
        b = tmp
        if b < c :
            tmp = b
            b = c
            c = tmp
print(b)