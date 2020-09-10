import sys

def solution():
    s = int(input())
    arr = [0] + list(map(int, sys.stdin.readline().split()))
    for i in range(1,s+1):
        arr[i] += arr[i-1]
    M = int(input())
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        print(arr[b] - arr[a-1])

solution()