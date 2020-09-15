from itertools import combinations

def solution():
    while True:
        arr = list(map(int, input().split()))
        if arr[0] == 0:
            return
        comb = arr[1:]
        for combination in combinations(comb, 6):
            print(*combination)
        print()

solution()