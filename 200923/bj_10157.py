def solution():
    C, R = map(int, input().split())
    K = int(input())
    result = [1,1]
    if K > C*R: print(0)
    else:
        K -= R
        result[1] += R-1
        for i in range(1, C*R):
            if i%2:
                if K <= 0:
                    result[1] += K
                    break
                K -= C-i
                result[0] += C-i
                if K <= 0:
                    result[0] += K
                    break
                K -= R-i
                result[1] -= R-i
            else:
                if K <= 0:
                    result[1] -= K
                    break
                K -= C - i
                result[0] -= C - i
                if K <= 0:
                    result[0] -= K
                    break
                K -= R - i
                result[1] += R - i
        print(*result)
solution()