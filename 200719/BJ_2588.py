A = input()
B = input()
A = int(A)
B = int(B)
C = B%10
D = B%100
print(A*C)
print(int(A*(D-C)/10))
print(int(A*(B-D)/100))
print(A*B)