n = int(input())
arr = [input() for i in range(n)]
ans = []
for i in range(n):
    se = set()
    for j in range(n):
        if arr[i][j] == 'Y':
            se.add(j)
            for k in range(n):
                if arr[j][k] == 'Y' and k != i:
                    se.add(k)
    ans.append(len(se))
print(max(ans))