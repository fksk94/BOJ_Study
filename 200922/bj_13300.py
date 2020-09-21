T, N = map(int, input().split())
r = 0
dict_room = {0:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0}, 1:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0}}
for i in range(T):
    a, b = map(int, input().split())
    dict_room[a][b] += 1
for i in dict_room.values():
    for j in i.values():
       r += (j-1)//N + 1
print(r)