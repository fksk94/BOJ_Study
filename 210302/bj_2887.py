from sys import stdin
input = stdin.readline
import sys
sys.setrecursionlimit(200000)


def parent(node):
    if node == Nodes[node]:
        return node
    else:
        Nodes[node] = parent(Nodes[node])
        return Nodes[node]

N = int(input())
arr = [list(map(int, input().split())) + [_] for _ in range(1,N+1)]
a = sorted(arr, key=lambda x:x[0])
b = sorted(arr, key=lambda x:x[1])
c = sorted(arr, key=lambda x:x[2])

i = 0
Union = []
while i < N-1:
    cost = abs(a[i][0] - a[i+1][0])
    Union.append((cost, a[i][3], a[i+1][3]))
    cost = abs(b[i][1] - b[i + 1][1])
    Union.append((cost, b[i][3], b[i + 1][3]))
    cost = abs(c[i][2] - c[i + 1][2])
    Union.append((cost, c[i][3], c[i + 1][3]))
    i += 1
Union.sort()
Nodes = [-1] * len(Union)
all_cost = 0
for cost, s, e in Union:
    if Nodes[s] == -1 and Nodes[e] == -1:
        Nodes[s] = s
        Nodes[e] = s
        all_cost += cost
    elif Nodes[s] == -1:
        Nodes[s] = parent(e)
        all_cost += cost
    elif Nodes[e] == -1:
        Nodes[e] = parent(s)
        all_cost += cost
    else:
        s_p = parent(s)
        e_p = parent(e)
        if s_p == e_p:
            continue
        else:
            Nodes[e_p] = s_p
            all_cost += cost

print(all_cost)

