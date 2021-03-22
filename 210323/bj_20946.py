import math

N = int(input())
res = [N]
before = -1
while len(res) != before:
    before = len(res)
    max_N = math.floor((res[-1]) ** (1/2))
    arr = []
    for i in range(2, max_N+1):
        if res[-1] % i == 0:
            arr.append(i)
            arr.append(res[-1]//i)
    arr.sort()
    for i in arr:
        max_i = math.floor((i) ** (1 / 2))
        tmp = []
        for k in range(2, max_i + 1):
            if i % k == 0:
                break
        else:
            continue
        tt = res[-1] // i
        res[-1] = i
        res.append(tt)
        break

if res:
    check = False
    max_N = math.floor((res[-1]) ** (1/2))
    for i in range(2, max_N+1):
        if res[-1] % i == 0:
            check = True
            break
    if check:
        for dk in res:
            print(dk, end=" ")
    else:
        if len(res) == 1:
            print(-1)
        else:
            gg = res.pop()
            res[-1] *= gg
            for dk in res:
                print(dk, end=" ")
else:
    print(-1)