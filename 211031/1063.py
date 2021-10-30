a, b, n = input().split()

x1, y1 = ord(a[0]), int(a[1])
x2, y2 = ord(b[0]), int(b[1])

for _ in range(int(n)):
    m = input()
    tx = x1
    ty = y1
    tx2 = x2
    ty2 = y2
    for i in m:
        if i == 'R':
            tx += 1
        elif i == 'L':
            tx -= 1
        elif i == 'B':
            ty -= 1
        else:
            ty += 1
    if tx == x2 and ty == y2:
        tx2 += (tx - x1)
        ty2 += (ty - y1)

    if 65 <= tx2 <= 72 and 1 <= ty2 <= 8 and 65 <= tx <= 72 and 1 <= ty <= 8:
        x1 = tx
        y1 = ty
        x2 = tx2
        y2 = ty2

print(chr(x1) + str(y1))
print(chr(x2) + str(y2))