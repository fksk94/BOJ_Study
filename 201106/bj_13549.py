import heapq


def djst():
    while q:

        F = heapq.heappop(q)

        if F[1] * 2 <= 100000 and M[F[1] * 2] == float('inf'):
            heapq.heappush(q, (F[0], F[1] * 2))
            M[F[1]*2] = F[0]

        if F[1] + 1 <= 100000 and M[F[1] + 1] == float('inf'):
            heapq.heappush(q, (F[0] + 1, F[1] + 1))
            M[F[1] + 1] = F[0] + 1

        if F[1] - 1 >= 0 and M[F[1] - 1] == float('inf'):
            heapq.heappush(q, (F[0] + 1, F[1] - 1))
            M[F[1] - 1] = F[0] + 1


N, K = map(int, input().split())
M = [float('inf')] * 100001
q = [(0, N)]
M[N] = 0
djst()
print(M[K])
