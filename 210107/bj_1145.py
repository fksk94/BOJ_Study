from itertools import combinations

def GCD(a, b):
    if a%b:
        return GCD(b, a%b)
    else:
        return b

N = list(map(int, input().split()))
N.sort()
combination = combinations(N, 3)
rres = float('inf')

for comb in combination:
    tmp = GCD(comb[0], comb[1])
    res = comb[2] // GCD(comb[0] // tmp * comb[1], comb[2]) * comb[0] // tmp * comb[1]
    if res < rres:
        rres = res

print(rres)