li1 = []
li2 = []
for _ in range(3):
    x, y = map(int, input().split())
    li1.append(x)
    li2.append(y)

for i in range(3) :

    if li1.count(li1[i]) == 1 :
        x = li1[i]

    if li2.count(li2[i]) == 1 :
        y = li2[i]
print("{x} {y}".format(x = x, y = y))