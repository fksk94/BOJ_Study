import math
a = int(input())

for _ in range(a) :
    max_meter = 0
    li = list(map(int,input().split()))
    meter = math.sqrt((li[3] - li[0])**2 + (li[4] - li[1])**2)
    if li[2] > li[5] :
        max_meter = li[2]
        min_meter = li[5]
    else :
        max_meter = li[5]
        min_meter = li[2]

    if li[2] == li[5] and li[1] == li[4] and li[0] == li[3] :
        print(-1)
    elif math.isclose(meter, li[5]+li[2]) :
        print(1)
    elif li[2] + li[5] < meter :
        print(0)
    elif li[2] + li[5] > meter :
        if min_meter >= meter:
            if math.isclose(max_meter, meter + min_meter):
                print('1')
            elif max_meter > meter + min_meter :
                print('0')
            else:
                print('2')
        elif min_meter < meter :
            if math.isclose(max_meter, meter + min_meter):
                print('1')
            elif max_meter > meter + min_meter :
                print('0')
            else:
                print('2')