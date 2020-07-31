cro_alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

s = input()
tmp = []
sum_i = 0
for i in cro_alp :
    sum_i += s.count(i)
    if s.count(i) > 0 :
        tmp.append(i)
    if i == 'dz=' :
        sum_i -= s.count(i)

for j in tmp:
    if 'dz=' == j :
        sum_i -= s.count('dz=')
        continue
    else :
        s = s.replace(j,'')

for i in s :
    sum_i += 1
    s = s.replace(i,'')

print(sum_i)