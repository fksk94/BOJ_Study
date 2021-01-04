from sys import stdin
input = stdin.readline

def multifliy(a, b):
    R = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            for z in range(N):
                R[i][j] += a[i][z] * b[z][j]
                R[i][j] %= 1000
    return R

def find(cnt):
    if dic.get(cnt):
        return dic.get(cnt)
    else:
        if cnt % 2:
            tmp = multifliy(find(cnt // 2), find(cnt // 2 + 1))
            dic[cnt] = tmp
            return tmp
        else:
            tmp = multifliy(find(cnt // 2), find(cnt // 2))
            dic[cnt] = tmp
            return tmp

N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]

A2 = multifliy(A, A)
A4 = multifliy(A2, A2)
A5 = multifliy(A4, A)
dic = {
    1: A,
    2: A2,
    4: A4,
    5: A5,
}

ans = find(M)

for i in range(len(ans)):
    for j in range(len(ans)):
        ans[i][j] %= 1000

for i in ans:
    print(*i)