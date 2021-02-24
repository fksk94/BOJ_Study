from sys import stdin
input = stdin.readline
import sys
sys.setrecursionlimit(20000)


def union1(arr, num):
    if num == 0:
        res[0] = max(res[0], max([max(i) for i in arr]))
        return
    for i in range(N):
        before = 0
        cnt = N-1
        for j in range(N-1, -1, -1):
            if before and before == arr[i][j]:
                arr[i][cnt+1] *= 2
                before = 0
                arr[i][j] = 0
                continue
            if arr[i][j] != 0:
                before = arr[i][j]
                arr[i][j] = 0
                arr[i][cnt] = before
                cnt -= 1
    union1([i[:] for i in arr], num - 1)
    union2([i[:] for i in arr], num - 1)
    union3([i[:] for i in arr], num - 1)
    union4([i[:] for i in arr], num - 1)

def union2(arr, num):
    if num == 0:
        res[0] = max(res[0], max([max(i) for i in arr]))
        return
    for i in range(N):
        before = 0
        cnt = 0
        for j in range(N):
            if before and before == arr[i][j]:
                arr[i][cnt-1] *= 2
                before = 0
                arr[i][j] = 0
                continue
            if arr[i][j] != 0:
                before = arr[i][j]
                arr[i][j] = 0
                arr[i][cnt] = before
                cnt += 1
    union1([i[:] for i in arr], num - 1)
    union2([i[:] for i in arr], num - 1)
    union3([i[:] for i in arr], num - 1)
    union4([i[:] for i in arr], num - 1)

def union3(arr, num):
    if num == 0:
        res[0] = max(res[0], max([max(i) for i in arr]))
        return
    for i in range(N):
        before = 0
        cnt = N-1
        for j in range(N-1, -1, -1):
            if before and before == arr[j][i]:
                arr[cnt+1][i] *= 2
                before = 0
                arr[j][i] = 0
                continue
            if arr[j][i] != 0:
                before = arr[j][i]
                arr[j][i] = 0
                arr[cnt][i] = before
                cnt -= 1
    union1([i[:] for i in arr], num - 1)
    union2([i[:] for i in arr], num - 1)
    union3([i[:] for i in arr], num - 1)
    union4([i[:] for i in arr], num - 1)

def union4(arr, num):
    if num == 0:
        res[0] = max(res[0], max([max(i) for i in arr]))
        return
    for i in range(N):
        before = 0
        cnt = 0
        for j in range(N):
            if before and before == arr[j][i]:
                arr[cnt-1][i] *= 2
                before = 0
                arr[j][i] = 0
                continue
            if arr[j][i] != 0:
                before = arr[j][i]
                arr[j][i] = 0
                arr[cnt][i] = before
                cnt += 1
    union1([i[:] for i in arr], num - 1)
    union2([i[:] for i in arr], num - 1)
    union3([i[:] for i in arr], num - 1)
    union4([i[:] for i in arr], num - 1)

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
res = [0]
union1([i[:] for i in a], 5)
union2([i[:] for i in a], 5)
union3([i[:] for i in a], 5)
union4([i[:] for i in a], 5)
print(res[0])