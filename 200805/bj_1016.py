s1, s2 = map(int, input().split())
r = [False for i in range(s1, s2 + 1)]
s = [i ** 2 for i in range(2, 1000001)]

for i in s:
    if s1 // i * i < s1 :
        n = (s1 // i + 1) * i - s1
    else :
        n = round(s1 / i) * i - s1
    while n <= s2 - s1:
        r[n] = True
        n += i

result = 0

for i in r:
    if not i :
        result += 1

print(result)