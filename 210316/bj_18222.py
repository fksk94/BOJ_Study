a = int(input()) - 1
cnt = 0
while(a > 0):
    cnt += a & 1
    a >>= 1
print(cnt & 1)