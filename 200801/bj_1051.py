import copy

s = list(map(int, input().split()))

i = 0

li = []
li2 = []

while i < s[0]:
    s1 = list(input())
    li.append(s1)
    i += 1
li2 = copy.deepcopy(li)
i = 0


if s[0] > s[1] :
    min_s = s[1]
else :
    min_s = s[0]

n = 0
result = [1]

while n < min_s :
    li = copy.deepcopy(li2)

    for i in li :
        for j in i :
            if (i.index(j)+n) < s[1] :
                if (li.index(i)+n) < s[0] :
                    if j == i[(i.index(j)+n) % s[1]] :
                        if j == li[(li.index(i)+n) % s[0]][i.index(j)] :
                            if j == li[(li.index(i)+n) % s[0]][(i.index(j)+n) % s[1]] :
                                result.append((n+1)*(n+1)) # 여기네 마지막에서 3*3을 무조건 하구나.
            li[li.index(i)][i.index(j)] = '확인'
    n +=1

print(max(result))

    