from collections import deque

a, b, c = map(int, input().split())
arr = list(map(int, input().split()))
narr = deque([b])

for i in range(a):
    j = 0
    ln = len(narr)
    while j < ln:
        nb = narr.popleft()
        if 0 <= nb - arr[i] <= c:
            narr.append(nb - arr[i])
        if 0 <= nb + arr[i] <= c:
            narr.append(nb + arr[i])
        j += 1
    narr = deque(set(narr))

if narr:
    print(max(narr))
else:
    print(-1)