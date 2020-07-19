import sys

j = int(input())
i = int(0)
sum = []
c = []
d = []
while i < j :
    a, b = map(int, sys.stdin.readline().split())
    sum.append(a+b)
    c.append(a)
    d.append(b)
    i += 1
i = int(0)
for z in sum :
    i += 1
    print(f"Case #{i}: {c[i-1]} + {d[i-1]} = {z}")