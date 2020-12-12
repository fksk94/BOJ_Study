def select(a, l, r):
    pivot = a[l]
    low = l
    high = r + 1
    while True:
        while True:
            low += 1
            if low > r or a[low] > pivot:
                break
        while True:
            high -= 1
            if high < l or a[high] <= pivot:
                break
        if high + 1 == low:
            break
        a[low], a[high] = a[high], a[low]
    a[l], a[high] = a[high], a[l]
    return high

def kth(a, k) :
    s = 0
    e = len(a)-1
    while True:
        p_idx = select(a, s, e)
        if k-1 > p_idx:
            s = p_idx+1
        elif k-1 < p_idx:
            e = p_idx-1
        else:
            return a[p_idx]