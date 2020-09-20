from itertools import combinations

arr = list(combinations([int(input()) for i in range(9)], 7))
for i in range(len(arr)):
    if sum(arr[i]) == 100:
        print(*sorted(arr[i]), sep='\n')
        break