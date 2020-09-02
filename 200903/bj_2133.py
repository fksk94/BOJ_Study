i = int(input())

dict_tile = {
    0 : 1,
    2 : 3,
    4 : 11
}
for n in range(6, 31, 2) :
    dict_tile[n] = 3 * dict_tile[n - 2]
    for j in range(n-4, -1,-2) :
        dict_tile[n] += dict_tile[j] * 2
if i%2 :
    print(0)
else :
    print(dict_tile[i])