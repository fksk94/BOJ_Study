n = int(input())
for j in range(n) :
    S = input().split()
    max_S = int(S[0])
    list_S = list(S[1])

    for i in list_S :
        print(str(i)*max_S, end='')
    print('')
