import math

s = int(input())

for i in range(s) :
    n, m = map(int, input().split())
    result = 0
    if m == n :
        result = math.factorial(m) // math.factorial(n)
    if n < m :
        result = math.factorial(m) // math.factorial(n) // math.factorial(m-n)
    print(result)