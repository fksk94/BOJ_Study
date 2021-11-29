T = int(input())
s = 2
for i in range(T-1):
    s = (s * 3 + 2) % 1000000007
print(s)