def a():
    row = ['A', 'B', 'C', 'D', 'E', 'F']
    col = list(map(str, range(1, 7)))
    s = input()
    sx = row.index(s[0])
    sy = col.index(s[1])
    dxy = [(1, 2), (2, 1), (-2, 1), (-1, 2), (1, -2), (2, -1), (-1, -2), (-2, -1)]
    check = set([s])
    for _ in range(35):
        nxy = input()
        check.add(nxy)
        for i in range(8):
            rx = sx + dxy[i][0]
            ry = sy + dxy[i][1]
            if 0 <= rx < 6 and 0 <= ry < 6 and nxy == row[rx] + col[ry]:
                sx, sy = rx, ry
                break
        else:
            return 'Invalid'

    for i in range(8):
        rx = sx + dxy[i][0]
        ry = sy + dxy[i][1]
        if 0 <= rx < 6 and 0 <= ry < 6 and s == row[rx] + col[ry]:
            break
    else:
        return 'Invalid'

    if len(check) != 36:
        return 'Invalid'
    return 'Valid'

print(a())