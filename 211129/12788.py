from sys import stdin
input = stdin.readline

T = int(input())
a,b = map(int, input().split())
c = list(map(int, input().split()))
c.sort(reverse=True)
s = 0
for i in range(T):
    s += c[i]
    if s >= a*b:
        print(i+1)
        break
else:
    print('STRESS')