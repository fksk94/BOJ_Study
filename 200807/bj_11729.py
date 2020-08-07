def hanoi(n, from_stick, to_stick, empty_stick):
    global count
    if n == 1 :
        print("{from_stick} {to_stick}".format(from_stick =from_stick, to_stick = to_stick))
        return
    if n == 0 :
        return
    hanoi(n-1, from_stick, empty_stick, to_stick)
    hanoi(1, from_stick, to_stick, empty_stick)
    hanoi(n-1, empty_stick, to_stick, from_stick)

s = int(input())

print(2**s-1)
hanoi(s, 1, 3, 2)
