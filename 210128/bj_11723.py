from sys import stdin
input = stdin.readline

N = int(input())
a = set()
for i in range(N):
    order = input().rstrip().split()
    if len(order) > 1:
        order[1] = int(order[1])
    if order[0] == 'add':
        a.add(order[1])
    elif order[0] == 'remove':
        a.discard(order[1])
    elif order[0] == 'check':
        if order[1] in a:
            print(1)
        else:
            print(0)
    elif order[0] == 'toggle':
        try:
            a.remove(order[1])
        except:
            a.add(order[1])
    elif order[0] == 'all':
        a = set(range(1,21))
    else:
        a = set()
