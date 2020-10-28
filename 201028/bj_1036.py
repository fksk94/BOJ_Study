def find(n):
    if n < 10:
        return str(n)
    else:
        return chr(n+55)

# 테케 갯수 입력
T = int(input())
# 배열, 결과 초기화, 입력
res = 0
a = [input() for i in range(T)]
K = int(input())
d = [find(i) for i in range(36)]

# 바꾸기
for _ in range(K):
    rrsum = []
    for k in range(len(d)):
        rsum = 0
        for i in range(T):
            for j in range(len(a[i])):
                if a[i][j] == d[k]:
                    rsum += 35 * (36 ** (len(a[i]) - j - 1))
                else:
                    rsum += int(a[i][j], 36) * (36 ** (len(a[i]) - j - 1))
        rrsum.append(rsum)
    tmp = rrsum.index(max(rrsum))
    d.pop(tmp)

for i in range(T):
    for j in range(len(a[i])):
        if a[i][j] in d:
            res += int(a[i][j], 36) * (36 ** (len(a[i]) - j - 1))
        else:
            res += 35 * (36 ** (len(a[i]) - j - 1))

s = ''
while res:
    res, num = divmod(res, 36)
    s =  find(num) + s
if s:
    print(s)
else:
    print(0)