from sys import stdin
# stdin = open('input.txt', 'r')
input = stdin.readline
import heapq

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    for j in range(M):
        a, b = map(int, input().split())
    print(N - 1)