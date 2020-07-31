S = list(input())
li = []
i = 97
while i < 123 :
    for j in S :
        if j == chr(i) :
            li.append(S.index(j))
            break
    else :
        li.append(-1)
    i += 1
for i in li :
    print(i, end=' ')