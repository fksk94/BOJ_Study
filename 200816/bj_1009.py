s = int(input())

for i in range(s):
    n, m = map(int, input().split())
    n = n%10
    if m%4 == 0 :
        m = 4
    else :
        m = m%4
    result = (n**m)%10
    if result == 0 :
        print(10)
    else :
        print(result)