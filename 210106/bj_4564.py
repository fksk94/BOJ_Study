from sys import stdin
input = stdin.readline

while True:
    a = input().rstrip()
    if a == '0':
        break
    print(a, end=' ')
    while len(a) != 1:
        res = 1
        for i in a:
            res *= int(i)
        print(res, end=' ')
        a = str(res)
    print()