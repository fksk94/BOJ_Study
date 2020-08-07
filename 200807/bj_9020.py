s = int(input())

max_primes = 10001
primes = [False, False] + [True] * (max_primes - 2)
primes_num = []

for i in range(2, len(primes)):
    if primes[i] == True:
        for j in range(i * 2, len(primes), i):
            primes[j] = False
        primes_num.append(i)

for z in range(s):
    n = int(input())
    min_dict = {}
    min_value = 10001
    for i in primes_num:
        if primes[n - i] == True and primes[i] == True:
            min_dict[i] = n - i

    for key, value in min_dict.items():
        if 0 <= key - value < min_value:
            min_value = key - value
            result1, result2 = key, value
    print('{result2} {result1}'.format(result2 = result2, result1 = result1))