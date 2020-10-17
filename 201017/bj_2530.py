c, a, b = map(int,input().split())
N = int(input())
b += N
a += b // 60
b = b % 60
c += a//60
a = a % 60
c = c % 24
print(c, a, b)