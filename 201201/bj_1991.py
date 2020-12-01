def preorder(check):
    print(check, end='')
    if dic[check][0] != '.':
        preorder(dic[check][0])
    if dic[check][1] != '.':
        preorder(dic[check][1])

def inorder(check):
    if dic[check][0] != '.':
        inorder(dic[check][0])
    print(check, end='')
    if dic[check][1] != '.':
        inorder(dic[check][1])

def postorder(check):
    if dic[check][0] != '.':
        postorder(dic[check][0])
    if dic[check][1] != '.':
        postorder(dic[check][1])
    print(check, end='')

N = int(input())

dic = {}
for i in range(N):
    arr = list(input().split())
    dic[arr[0]] = arr[1:]

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()