T = int(input())
arr = list(map(int, input().split()))
C = int(input())
for i in range(C):
    a, b = map(int, input().split())
    if a == 1:
        for j in range(b-1, len(arr), b):
            arr[j] = arr[j]^1
    else:
        b = b - 1
        arr[b] = arr[b] ^ 1
        for j in range(1, min(len(arr)-b,b+1)):
            if arr[b-j] == arr[b+j]:
                arr[b-j] = arr[b-j]^1
                arr[b + j] = arr[b + j] ^ 1
            else:
                break
print(arr[0], end=' ')
for i in range(1, len(arr)):
    if i%20 == 0 :
        print()
    print(arr[i], end=' ')
