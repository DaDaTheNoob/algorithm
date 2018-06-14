def mergearry(a, b):
    i = 0
    j = 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    return c


def mergesort(l):
    m = int(len(l)/2)
    a = l[0:m]
    b = l[m:len(l)]
    if len(a) > 1:
        a1 = mergesort(a)
    else:
        a1 = a
    if len(b) > 1:
        b1 = mergesort(b)
    else:
        b1 = b
    c = mergearry(a1, b1)
    return c