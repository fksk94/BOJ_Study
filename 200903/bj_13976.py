def getPower(matrix, N) :
    if N == 1 :
        return matrix
    else :
        if N%2 == 0 :
            part = getPower(matrix, N//2)
            return multi(part, part)
        else :
            return multi(getPower(matrix, N-1), matrix)

def multi(A, B) :
    result = [[0, 0],[0, 0]]
    result[0][0] = (((A[0][0] * B[0][0]) % 1000000007) + ((A[0][1] * B[1][0]) % 1000000007 + 1000000007)) % 1000000007
    result[0][1] = (((A[0][0] * B[0][1]) % 1000000007) + ((A[0][1] * B[1][1]) % 1000000007 + 1000000007)) % 1000000007
    result[1][0] = (((A[1][0] * B[0][0]) % 1000000007) + ((A[1][1] * B[1][0]) % 1000000007 + 1000000007)) % 1000000007
    result[1][1] = (((A[1][0] * B[0][1]) % 1000000007) + ((A[1][1] * B[1][1]) % 1000000007 + 1000000007)) % 1000000007
    return result

def jjin_multi(A,B) :
    a = ((A[0][0] * B[0] % 1000000007) + (A[0][1] * B[1] % 1000000007)) % 1000000007
    return a


i = int(input())

if i%2 :
    print(0)

elif i == 2 :
    print(3)

else :
    print(jjin_multi(getPower([[4,-1],[1,0]], i//2-1), [3, 1]))


