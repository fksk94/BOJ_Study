from sys import stdin
input = stdin.readline

s = input().rstrip()
bomb = input().rstrip()

S = []

i = 0
while i < len(s):
    S.append(s[i])
    for j in range(len(S)-1, len(S)-1-len(bomb), -1):
        if S[j] != bomb[-len(S)+j]:
            break
    else:
        for j in range(len(bomb)):
            S.pop()
    i += 1

if S:
    print("".join(S))
else:
    print("FRULA")
