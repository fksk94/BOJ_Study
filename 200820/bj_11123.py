import sys
sys.setrecursionlimit(100000)
s = int(input())

# 앞뒤 옆들이 #이면 remove를 한다.
# remove는 재귀로 사용한다.
def remove(n, m) :
    if arr[n][m] == '#' :
        arr[n][m] = '.'
        remove(n - 1, m)
        remove(n + 1, m)
        remove(n, m - 1)
        remove(n, m + 1)
    return


for _ in range(1, s+1) :
    count = 0
    n, m = map(int, sys.stdin.readline().split())
    arr = [['.']*(m+2)]
    arr += [['.'] for i in range(n)]
    arr += [['.'] * (m + 2)]

    for a in range(1, n+1) :
        arr[a].extend(list(sys.stdin.readline().rstrip()))
        arr[a].append('.')
    for i in range(1, n+1) :
        for j in range(1, m+1) :
            if arr[i][j] == '#' :
                remove(i, j)
                count += 1
    print(count)