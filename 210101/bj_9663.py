N = int(input())
a, b, c = [False]*N, [False]*(2*N-1), [False]*(2*N-1)
count=0
 
def nqueen(n):
    global count
    if n == N:
        count+=1
        return
    if n!=0:
        for i in range(N):
            if not (a[i] or b[n+i] or c[n-i+N-1]):
                a[i] = b[n+i] = c[n-i+N-1] = True
                nqueen(n+1)
                a[i] = b[n+i] = c[n-i+N-1] = False
    else:
        for i in range(N//2):
            if not (a[i] or b[n+i] or c[n-i+N-1]):
                a[i] = b[n+i] = c[n-i+N-1] = True
                nqueen(n+1)
                a[i] = b[n+i] = c[n-i+N-1] = False
        count*=2
        if N%2==1:
            a[(N//2)] = b[(N//2)] = c[-(N//2)+N-1] = True
            nqueen(n+1)
            a[(N//2)] = b[(N//2)] = c[-(N//2)+N-1] = False
             
nqueen(0)
print(count)