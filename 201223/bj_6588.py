max_primes = 1000001
primes = [False, False] + [True] * (max_primes - 2)
primes_num = []

for i in range(2, len(primes)):
    if primes[i] == True:
        for j in range(i * 2, len(primes), i):
            primes[j] = False
        primes_num.append(i)

while True:
    n = int(input())
    if n == 0:
        break
    check = False
    for i in primes_num:
        if primes[n - i] == True and primes[i] == True:
            min_val = (n-i, i)
            check = True
            break
    else:
        print("Goldbach's conjecture is wrong.")
    if check:
        print('{} = {result2} + {result1}'.format(n, result2 = min_val[1], result1 = min_val[0]))