from sys import stdin
input = stdin.readline

def find(N):
    for i in range(500000):
        MN = str(max(0, N - i))
        PN = str(N + i)
        for j in MN:
            if errors[int(j)]:
                break
        else:
            return len(MN) + i
        for j in PN:
            if errors[int(j)]:
                break
        else:
            return len(PN) + i
    return 500000

N = int(input())
M = int(input())
a = list(map(int, input().split()))
errors = [False] * 10
for i in a:
    errors[i] = True
print(min(abs(N-100), find(N)))