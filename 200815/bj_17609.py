import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n) :
    arr.append(sys.stdin.readline().rstrip())

for i in range(n):
    if ''.join(reversed(arr[i])) == arr[i] :
        print(0)
    else :
        tmp = ''.join(reversed(arr[i]))
        for j in range(len(arr[i])//2):
            if tmp[j] != arr[i][j]:
                s1 = arr[i][:j]+arr[i][j+1:]
                s2 = tmp[:j]+tmp[j+1:]
                if ''.join(reversed(s1)) == s1 or ''.join(reversed(s2)) == s2 :
                    print(1)
                    break
                else :
                    print(2)
                    break