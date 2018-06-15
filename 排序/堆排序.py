def heap_mod(l, i, k):
    left = 2*i+1
    right = 2*i+2
    if left < k and l[left] > l[i]:
        largest = left
    else:
        largest = i
    if right < k and l[right] > l[largest]:
        largest = right
    if largest != i:
        l[largest], l[i] = l[i], l[largest]
        if largest < int(k/2):
            heap_mod(l, largest, k)


def heap_cons(l, k):
    i = int(k/2)-1
    while i >=0:
        heap_mod(l, i, k)
        i -= 1


def heapsort(l, i):
    if i > 0:
        heap_cons(l, i)  
        l[0], l[i-1] = l[i-1], l[0]
        i -= 1
        heapsort(l, i)





l=[5,4,3,2,1,0]
heapsort(l, len(l))
print(l)