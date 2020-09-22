def solution():
    T = int(input())
    result = [0]*500
    for i in range(1, T+1):
        tmp = [T, i]
        j = 0
        while True:
            if tmp[j] - tmp[j+1] < 0:
                result[len(tmp)] = tmp
                break
            else:
                tmp.append(tmp[j] - tmp[j+1])
                j += 1
    for i in range(499,0,-1):
        if result[i]:
            print(i)
            print(*result[i])
            break
solution()