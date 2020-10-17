a, b = map(int,input().split())
N = int(input())
b += N
a += b // 60
b = b % 60
a = a % 24
print(a, b)