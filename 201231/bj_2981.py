from sys import stdin
import math
input = stdin.readline

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

N=int(input())
arr = [int(input()) for i in range(N)]
arr.sort()
tmp = arr[1] - arr[0]
for i in range(2, N):
    if tmp < (arr[i]-arr[i-1]):
        tmp = gcd((arr[i]-arr[i-1]), tmp)
    else:
        tmp = gcd(tmp, (arr[i] - arr[i - 1]))
ans = set()
for i in range(1, int(math.sqrt(tmp))+1):
    if tmp%i == 0:
        ans.add(i)
        ans.add(tmp//i)
print(*sorted(list(ans))[1:])