i = int(input())

dict_tile = {
    1 : 1,
    2 : 3,
    3 : 5
}
for n in range(4, 1001) :
    if n % 2:
        dict_tile[n] = dict_tile[n // 2] * dict_tile[n // 2 + 1] + 2 * (dict_tile[n // 2 - 1] * dict_tile[n // 2])
    else :
        dict_tile[n] = dict_tile[n//2] * dict_tile[n//2] + 2 * (dict_tile[n//2-1] * dict_tile[n//2-1])

print(dict_tile[i]%10007)