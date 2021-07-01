from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())
a = input().rstrip()
i = 0
cnt = 0
while i < M:
    if a[i] == "I":
        for j in range(i+1, i+2*N+1):
            if j >= M:
                i = j
                break
            if (j-i)%2 and a[j] == "O":
                continue
            elif (j-i)%2 == 0 and a[j] == "I":
                continue
            else:
                i = j
                break
        else:
            cnt += 1
            i = j
            while True:
                if i >= M-2:
                    i += 2
                    break
                if a[i+1] == "O" and a[i+2] == "I":
                    cnt += 1
                    i += 2
                else:
                    break
    else:
        i += 1
print(cnt)