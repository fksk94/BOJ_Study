S = input()
arr = []
for i in range(len(S)):
    arr.append((i, S[i:]))
arr.sort(key=lambda x:x[1])
for i, val in arr:
    print(val)