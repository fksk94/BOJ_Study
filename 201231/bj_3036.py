from sys import stdin
input = stdin.readline


def gcd(a, b):
    if a % b:
        return gcd(b, a%b)
    else:
        return b

N=int(input())
arr = list(map(int, input().split()))
for i in range(1, N):
    tmp = gcd(arr[0], arr[i])
    print(str(arr[0]//tmp)+'/'+str(arr[i]//tmp))