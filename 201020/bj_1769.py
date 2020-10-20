a = list(input())
cnt = 0
if len(a) == 1:
    sum = int(a[0])
else:
    while True:
        cnt += 1
        sum = 0
        for i in a:
            sum += int(i)
        if sum < 10:
            break
        else:
            a = str(sum)
print(cnt)
if sum == 3 or sum == 6 or sum == 9:
    print('YES')
else:
    print('NO')