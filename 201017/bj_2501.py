a, b = map(int,input().split())
seta = set()
for i in range(1, a//2+1):
    if a % i == 0:
        seta.add(i)
        seta.add(a//i)
abab = list(seta)
abab.sort()
if len(abab) >= b:
    print(abab[b-1])
else: 
    print(0)