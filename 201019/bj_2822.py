a = []
for i in range(8):
    a.append(int(input()))
s = sum(sorted(a)[3:])
a = list(enumerate(a))
a = sorted(a, key=lambda x:x[1])[3:]
print(s)
print(*[sorted(a)[i][0]+1 for i in range(5)])