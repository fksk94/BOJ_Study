import sys

for _ in range(4):
    arr = list(map(int, sys.stdin.readline().split()))
    if arr[2] < arr[4] or arr[3] < arr[5] or arr[6] < arr[0] or arr[7] < arr[1]:
        print('d')
        continue
    elif arr[2] == arr[4] and arr[3] == arr[5] or arr[6] == arr[0] and arr[7] == arr[1]:
        print('c')
        continue
    elif arr[1] == arr[7] and arr[2] == arr[4] or arr[6] == arr[0] and arr[5] == arr[3]:
        print('c')
        continue
    elif arr[2] == arr[4] and arr[3] > arr[5] or arr[2] > arr[4] and arr[3] == arr[5]:
        print('b')
        continue
    elif arr[6] > arr[0] and arr[7] == arr[1] or arr[6] == arr[0] and arr[7] > arr[1]:
        print('b')
        continue
    elif arr[1] < arr[7] and arr[2] == arr[4] or arr[1] == arr[7] and arr[2] > arr[4]:
        print('b')
        continue
    elif arr[6] > arr[0] and arr[5] == arr[3] or arr[6] == arr[0] and arr[5] < arr[3]:
        print('b')
        continue
    else:
        print('a')