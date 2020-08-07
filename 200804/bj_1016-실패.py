s = list(map(int, input().split()))

n_min = s[0]

n=1000001
'''
b = [False,False] + [True]*(n-2)

for i in range(2,n):
  if b[i]:
    for j in range(2*i, n, i):
        b[j] = False
'''
a = list(range(n_min, s[1]+1))

sum_i = 0


for i in range(2,n):
    for j in range(s[1]-n_min+1):
        if a[j] % (i*i) == 0 :
            a[j] = False

result = (s[1] - n_min + 1) - a.count(False)
print(result)