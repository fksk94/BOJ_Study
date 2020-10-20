a = int(input())
b= list(map(int, input().split()))
b.sort()
n = int(input())
for i in range(len(b)):
    if n == b[i]:
        print(0)
        break
    if n < b[i]:
        if i == 0:
            print((b[i] - n)*n-1)
            break
        print((b[i] - n)*(n-b[i-1])-1)
        break