from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
bundles = []
ones = []
for _ in range(M):
    bundle, one = map(int, input().split())
    bundles.append(bundle)
    ones.append(one)
bundle, one = min(bundles), min(ones)
if one * 6 < bundle:
    print(one * N)
else:
    print(min((one * (N % 6)) + ((N // 6) * bundle), (N // 6 + 1) * bundle))