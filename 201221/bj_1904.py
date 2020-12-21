def get_res(n):
    if n < 9:
        return arr[n]
    if n % 2:
        return ((get_res(n//2+1)**2) - (get_res(n//2-1)**2))
    else:
        return (get_res(n // 2) ** 2) + (get_res(n // 2 - 1) ** 2)
N = int(input())
arr = [0, 1, 2, 3, 5, 8, 13, 21, 34]
print(get_res(N)%15746)