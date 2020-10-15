S = int(input())
Ssum = 0
for i in range(1,S+2):
    Ssum += i
    if Ssum == S:
        print(i)
        break
    elif Ssum > S:
        print(i-1)
        break