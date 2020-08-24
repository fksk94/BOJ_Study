N, M = map(int, input().split())

arr = [1, 2, 3, 4, 5, 6, 7, 8]
result = []
real_result = []

def backTracking(cir_count) :
    global M, N

    if M == cir_count :
        for i in range(M-1):
            if arr[i] > arr[i + 1]:
                return
        for j in arr[0:M]:
            print(j, end=' ')
        print()
        return


    for i in range(1, N+1) :
        if cir_count >= 1 and arr[cir_count-1] > i :
            continue
        arr[cir_count] = i
        backTracking(cir_count+1)

backTracking(0)