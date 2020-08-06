x, y, w, h = map(int, input().split())

min_meter = 0
min_meter2 = 0
if w - x > x :
    min_meter = x
else :
    min_meter = w - x

if h - y > y :
    min_meter2 = y
else :
    min_meter2 = h - y

if min_meter > min_meter2 :
    print(min_meter2)
else :
    print(min_meter)