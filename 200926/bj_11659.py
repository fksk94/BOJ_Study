import sys
def solution():
    N, M = map(int, sys.stdin.readline().split())
    arr = [0]+list(map(int, sys.stdin.readline().split()))
    for i in range(1, N):
        arr[i+1] = arr[i] + arr[i+1]
    
    for i in range(M):
        s, e = map(int, sys.stdin.readline().split())
        print(arr[e] - arr[s-1])
solution()