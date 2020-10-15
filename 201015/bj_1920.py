import sys, math

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
M = int(input())
check = list(map(int, sys.stdin.readline().split()))
for i in check:
    a = N-1
    b = 0
    k = 0
    j = a
    while k <= math.log2(N) + 10:
        if i < arr[j]:
            j, a = (j + b)//2, j
        elif i > arr[j]:
            j, b = (j+a)//2, j
        else:
            print(1)
            break
        k += 1
    else:
        print('0')