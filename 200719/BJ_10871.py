a, b = map(int, input().split())
j = int(0)
temp = list(map(int, input().split()))
while j < a :
    if temp[j] < b :
        print(f"{temp[j]} ", end='')
    j += 1