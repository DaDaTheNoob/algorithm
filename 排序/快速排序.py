def partition(l, b, e):
    base = l[e-1]
    i = b-1
    j = b
    while j < e-1:
        if l[j] <= base:
            i += 1
            l[i], l[j] = l[j], l[i]
        j += 1
    l[i+1], l[e-1] = l[e-1], l[i+1]
    return i+1


def quicksort(l, b, e):
    if b < e:
        q = partition(l, b, e)
        quicksort(l, b, q)
        quicksort(l, q+1, e)