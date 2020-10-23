from itertools import permutations

a, b = map(int, input().split())
arr = list(map(int, input().split()))
for i in sorted(permutations(arr, b)):
    print(*i)