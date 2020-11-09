def BF():
    for i in range(1, N + 1):
        for j in range(1, N+1):
            for E, T in network[j]:
                # print(sections)
                if sections[j] + T < sections[E]:
                    sections[E] = sections[j] + T
                    if i == N:
                        return 'YES'
    return 'NO'


TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    sections = [1e9] * (N+1)
    network = [[] for i in range(N+1)]
    for i in range(M):
        S, E, T = map(int, input().split())
        network[S].append([E, T])
        network[E].append([S, T])
    for i in range(W):
        S, E, T = map(int, input().split())
        network[S].append([E, -T])
    # print(network)
    print(BF())