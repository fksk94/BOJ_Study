j = int(input())
result = []
i = int(0)
while i < j :
    a, b = map(int, input().split())
    result.append(a+b)
    i +=1
for z in result :
    print(z)