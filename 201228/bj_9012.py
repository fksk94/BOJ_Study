from sys import stdin
input = stdin.readline

N = int(input())
for i in range(N):
    A = input().rstrip()
    cnt1, cnt2 =0, 0
    for j in range(len(A)):
        if A[j] == ')':
            cnt1+=1
        else:
            cnt2+=1
        if cnt1 > cnt2:
            print('NO')
            break
    else:
        if cnt1 == cnt2:
            print('YES')
        else:
            print('NO')