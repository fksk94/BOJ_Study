T = list(input())
cnt = 0
for i in range(len(T)):
    if T[i] == 'Y':
        for j in range(i, len(T), i+1):
            if T[j] == 'N':
                T[j] = 'Y'
            else:
                T[j] = 'N'
        cnt += 1
print(cnt)