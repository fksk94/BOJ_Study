import collections

s = list(input())
s2 = []
for i in s :
    if ord(i) > 96 :
        s2.append(chr(ord(i)-32))
    else :
        s2.append(i)
dic = collections.Counter(s2)
max_num = 0
sum_num = 0


for key, value in dic.items() :
    if value > max_num :
        max_num = value
        max_char = key
for value in dic.values() :
    if value == max_num :
        sum_num += 1
        if sum_num >= 2 :
            print('?')
            break
    else :
        continue
else :
    print(max_char)