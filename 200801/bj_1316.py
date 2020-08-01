n = int(input())

sum_i = 0
tmp = []
j = 0

for i in range(n) :
    s = list(input())
    a = set(s)
    s += ['as']

    while j < len(s)-1 :
        if s[j] != s[j+1] :
            tmp.append(s[j])
        j += 1
    if len(tmp) == len(a) :
        sum_i += 1
    j = 0
    tmp.clear()

print(sum_i)
    