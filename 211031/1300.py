a = int(input())
b = int(input())
e = b
s = 1
while True:
    cnt = 0
    m = (s+e) // 2
    for i in range(1, a+1):
        cnt += min(a, m//i)
    if cnt >= b:
        if e == m:
            break
        e = m
    elif cnt < b:
        s = m + 1

print(m)