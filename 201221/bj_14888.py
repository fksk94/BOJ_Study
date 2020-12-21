from itertools import permutations

def solution():
    T = int(input())
    arr = list(map(int, input().split()))
    ADD, MIN, MUL, DIV = map(int, input().split())
    max_res = -float('inf')
    min_res = float('inf')
    a = list(permutations((['+'] * ADD) + (['-'] * MIN) + (['*'] * MUL) + (['//'] * DIV), T-1))
    for i in a:
        tmp = arr[0]
        for j in range(len(i)):
            if i[j] == '+':
                tmp = tmp + arr[j+1]
            elif i[j] == '-':
                tmp = tmp - arr[j+1]
            elif i[j] == '*':
                tmp = tmp * arr[j+1]
            else:
                if tmp < 0:
                    tmp = -(abs(tmp) // arr[j+1])
                else:
                    tmp = tmp // arr[j + 1]
        if tmp > max_res:
            max_res = tmp
        if tmp < min_res:
            min_res = tmp
    print(max_res)
    print(min_res)
solution()