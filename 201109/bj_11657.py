def BF():
    for i in range(N + 1):
        for j in range(1, N+1):
            if sections[j] == float('inf'):
                continue
            for E, T in network[j]:
                if sections[j] + T < sections[E]:
                    sections[E] = sections[j] + T
                    if i == N:
                        print(-1)
                        return False
    return True


N, M = map(int, input().split())
sections = [float('inf')] * (N+1)
network = [[] for i in range(N+1)]
sections[1] = 0
for i in range(M):
    S, E, T = map(int, input().split())
    network[S].append([E, T])
if BF():
    for i in range(2, N+1):
        if sections[i] == float('inf'):
            print(-1)
        else:
            print(sections[i])