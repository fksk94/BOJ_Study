a= input().split(':')
res = 0
if 1 <= int(a[0]) <= 12:
    if 0 <= int(a[1]) <= 59:
        if 0 <= int(a[2]) <= 59:
            res += 2
if 1 <= int(a[1]) <= 12:
    if 0 <= int(a[0]) <= 59:
        if 0 <= int(a[2]) <= 59:
            res += 2
if 1 <= int(a[2]) <= 12:
    if 0 <= int(a[1]) <= 59:
        if 0 <= int(a[0]) <= 59:
            res += 2
print(res)