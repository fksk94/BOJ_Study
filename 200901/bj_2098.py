from itertools import combinations

def conv(n) :
    a = int(n)
    if a == 0 :
        a = float('inf')
    return a

def TSP(n) :
    for i in range(1, n) :
        arr_dict[(1 + (1<<i), i)] = arr[0][i]
    for i in range(2, n+1) :
        for combination in combinations(range(1, n), i) :
            goto = 1
            for j in combination :
                goto += 1<<j
            for j in combination :
                compare_value = float('inf')
                for _ in combination :
                    if _ != 0 and _ != j :
                        if compare_value > arr_dict[(goto - (1 << j), _)] + arr[_][j] :
                            compare_value = arr_dict[(goto - (1 << j), _)] + arr[_][j]
                arr_dict[(goto, j)] = compare_value

    result = float('inf')
    for i in range(1, n) :
        result = min(result, arr_dict[((2<<n-1)-1),i] + arr[i][0])

    return result

arr = []
n = int(input())
for i in range(n) :
    arr.append(list(map(conv, input().split())))
arr_dict = {}
print(TSP(n))