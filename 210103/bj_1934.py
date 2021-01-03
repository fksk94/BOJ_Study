from sys import stdin

def GCD(a, b):
    if a % b:
        return GCD(b, a % b)
    else:
        return b


input = stdin.readline
N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    if b >= a:
        print(a // GCD(b, a) * b)
    else:
        print(a // GCD(a, b) * b)