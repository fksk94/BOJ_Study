import sys
from collections import deque

T = int(input())
for _ in range(T):
    sm, sc, si = map(int, sys.stdin.readline().split())
    arr = [0] * sm
    command = sys.stdin.readline().rstrip()
    data = deque(list(sys.stdin.readline().rstrip()))
    Loops = []
    X_Loops = set()
    n, i, j, cnt_s = 0, 0, 0, 0
    try:
        while True:
            if command[j] == '+':
                arr[i] += 1
                arr[i] = arr[i] % 256
            elif command[j] == '-':
                arr[i] -= 1
                arr[i] = arr[i] % 256
            elif command[j] == '>':
                i += 1
                i = i % sm
            elif command[j] == '<':
                i -= 1
                i = i % sm
            elif command[j] == '.':
                i = i
            elif command[j] == ',':
                if len(data):
                    arr[i] = ord(data.popleft())
                else:
                    arr[i] = 255
            elif command[j] == '[':
                tmp_cnt = 0
                for k in range(j + 1, len(command)):
                    if command[k] == '[':
                        tmp_cnt += 1
                    elif command[k] == ']':
                        if tmp_cnt:
                            tmp_cnt -= 1
                        else:
                            break
                Loops.append((j, k))
                if arr[i] == 0:
                    j = k - 1
            elif command[j] == ']':
                if arr[i] == 0:
                    X_Loops.add(Loops.pop())
                else:
                    j = Loops[len(Loops)-1][0]
            n += 1
            j += 1
            if n == 50000000:
                for X_L in X_Loops:
                    if X_L in Loops:
                        Loops.remove(X_L)
                print('Loops {} {}'.format(Loops[len(Loops)-1][0], Loops[len(Loops)-1][1]))
                break
    except:
        print('Terminates')
