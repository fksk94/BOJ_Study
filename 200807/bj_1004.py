s1 = int(input())

for i in range(s1) :
    x1, y1, x2, y2 = map(int, input().split())
    s2 = int(input())
    ccr = []
    for _ in range(s2):
        ccr.append(list(map(int, input().split())))
    count = 0
    for j in range(s2):
        com_a = (x1 - ccr[j][0])**2 + (y1 - ccr[j][1])**2
        com_b = (x2 - ccr[j][0])**2 + (y2 - ccr[j][1])**2

        if com_a == ccr[j][2]**2 and com_b == ccr[j][2]**2 :
            count += 2

        elif com_b >= ccr[j][2]**2 :
            if com_a <= ccr[j][2] ** 2:
                count += 1

        elif com_a >= ccr[j][2]**2 :
            if com_b <= ccr[j][2]**2 :
                count += 1

    print(count)