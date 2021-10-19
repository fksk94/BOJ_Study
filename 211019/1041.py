from sys import stdin

input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
n3 = [(0, 2, 1), (0, 1, 3), (0, 3, 4), (0, 4, 2), (5, 2, 1), (5, 1, 3), (5, 3, 4), (5, 4, 2)]
n2 = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (2, 4), (3, 4), (5, 1), (5, 2), (5, 3), (5, 4)]
n1 = [0, 1, 2, 3, 4, 5]

if n == 1:
    print(sum(arr) - max(arr))
else:
    sn3 = float('inf')
    for a, b, c in n3:
        sn3 = min(sn3, arr[a] + arr[b] + arr[c])
    
    sn2 = float('inf')
    for a, b in n2:
        sn2 = min(sn2, arr[a] + arr[b])
    
    sn1 = float('inf')
    for a in n1:
        sn1 = min(sn1, arr[a])
    
    print(sn3*4 + sn2*((n-2)*8+4) + sn1*((n-2)**2*5+(n-2)*4))