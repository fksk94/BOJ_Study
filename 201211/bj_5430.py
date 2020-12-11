from collections import deque
import sys


input = sys.stdin.readline
T = int(input())
for _ in range(T):
    method = input().rstrip()
    N = int(input())
    arr = input().rstrip().rstrip(']').lstrip('[').split(',')
    arr = deque(arr)
    err = False
    if arr[0] == '':
        arr.popleft()
        if 'D' in method:
            err = True
    i = 0
    cnt = 0
    while i < len(method) and err == False:
        if method[i] == 'R':
            cnt += 1
        else:
            if arr:
                if cnt%2:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                err = True
                break
        i += 1
    if err:
        print('error')
    else:
        if cnt%2:
            print("[" + ','.join(reversed(arr)) + "]")
        else:
            print("[" + ','.join(arr) + "]")


