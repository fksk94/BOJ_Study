import sys
sys.setrecursionlimit(2000)

def dfs(start) :
    if start in arr :
        return
    else :
        arr.append(start)
        if dict_route.get(start) :
            for i in dict_route[start]:
                dfs(i)
    return

def bfs(start) :
    if dict_route.get(start):
        for i in dict_route[start]:
            if i in arr :
                pass
            else :
                arr.append(i)
    return

max_route, numbers, start = map(int, input().split())
dict_route = {}
arr = []
sarr = []
for i in range(numbers) :
    a, b = map(int, input().split())
    sarr.append(a)
    sarr.append(b)
    if not dict_route.get(a) :
        dict_route[a] = [b]
    else :
        dict_route[a] += [b]
    if not dict_route.get(b) :
        dict_route[b] = [a]
    else :
        dict_route[b] += [a]

for i in dict_route.values() :
    i.sort()

dfs(start)
for i in arr :
    print(i, end=' ')
print()
arr = [start]
i = 0
try :
    while True :
        bfs(arr[i])
        i += 1
        if len(arr) == len(set(sarr)) :
            for i in arr:
                print(i, end=' ')
            break
except :
    print(start)

