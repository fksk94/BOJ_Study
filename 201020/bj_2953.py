b = []
for i in range(5):
    a = list(map(int, input().split()))
    b.append(sum(a))
b = sorted(list(enumerate(b)), key=lambda x:x[1])
print(b[len(b)-1][0]+1, b[len(b)-1][1])