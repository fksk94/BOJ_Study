s = int(input())

li = []
li2 = []
num = 0

for i in range(s):
    li.clear()
    a = int(input())
    b = int(input())
    for j in range(1, b+1) :
        li.append(j)

    for z in range(a) :
        sum_li = 0
        for j in li :
            sum_li += j
            li2.append(sum_li)
        li.clear()
        li = li2[:]
        li2.clear()
    num += 1
    print(max(li))