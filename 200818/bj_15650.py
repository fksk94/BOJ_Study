import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

confirm = [False] * 9
arr = [1, 2, 3, 4, 5, 6, 7, 8]
result = []
real_result = []

def backTracking(cir_count) :
    global M, N

    if M == cir_count :
        result.append(arr[0:M])
        return

    for i in range(1, N+1) :
        if confirm[i] != True :
            confirm[i] = True
            arr[cir_count] = i
            backTracking(cir_count+1)
            confirm[i] = False

backTracking(0)

for i in result :
    i.sort()
    if not i in real_result :
        real_result.append(i)
        for j in i :
            print(j, end=' ')
        print()