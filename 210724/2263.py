from sys import stdin, setrecursionlimit
setrecursionlimit(2000000)
input = stdin.readline


N = int(input())

def find(s, e, c):
    if s > e:
        return
    print(postOrder[e - c], end=" ")
    find(s, dic[postOrder[e - c]] - 1, c)
    find(dic[postOrder[e - c]] + 1, e, c + 1)


dic = dict()
inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))
for i in range(N):
    dic[inOrder[i]] = i

find(0, N-1, 0)