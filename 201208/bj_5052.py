from collections import defaultdict
import sys


def check():
    for num in arr:
        for i in range(len(num)-min_len+1):
            if dic.get(num[:len(num)-i]):
                return 'NO'
        else:
            dic[num] += 1
    return 'YES'

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())

    arr = [input().rstrip() for i in range(N)]
    arr.sort(key=lambda  x:len(x))
    min_len = len(arr[0])
    dic = defaultdict(int)

    print(check())