s = int(input())

n = 1
while s > 0 :
    tmp = s
    s -= n
    n += 1
if not n%2 :
    print(f"{n-tmp}/{tmp}")
else :
    print(f"{tmp}/{n-tmp}")