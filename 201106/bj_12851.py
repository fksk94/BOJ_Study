from collections import deque


def djst():
    cnt = 0
    while q:
        F = q.popleft()
        if F[1] * 2 <= 100000:
            tmp = min(F[0] + 1, M[F[1] * 2])
            if tmp == F[0] + 1:
                q.append((F[0]+1, F[1] * 2))
                M[F[1]*2] = tmp
        if F[1] + 1 <= 100000:
            tmp = min(F[0] + 1, M[F[1] + 1])
            if tmp == F[0] + 1:
                q.append((F[0] + 1, F[1] + 1))
                M[F[1] + 1] = tmp
        if F[1] - 1 >= 0:
            tmp = min(F[0] + 1, M[F[1] - 1])
            if tmp == F[0]+1:
                q.append((F[0] + 1, F[1] - 1))
                M[F[1] - 1] = tmp
        if F[1] - 1 == K and M[K] == F[0] + 1:
            cnt += 1
        if F[1] * 2 == K and M[K] == F[0] + 1:
            cnt += 1
        if F[1] + 1 == K and M[K] == F[0] + 1:
            cnt += 1

    return cnt


N, K = map(int, input().split())
M = [float('inf')] * 100001
q = deque([(0, N)])
M[N] = 0
tmp = djst()
print(M[K])
print(max(tmp, 1))