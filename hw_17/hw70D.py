#70D
qcomps=0
qmoves=0
def quicksort(a):
    global qcomps
    global qmoves
    less = []
    equal = []
    greater = []
    qcomps+= len(a)
    if len(a) > 1:
        pivot = a[len(a)//2]
        for x in a:
            qcomps+=1
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        qmoves+=1
        return quicksort(less)+equal+quicksort(greater)
    else:
        return a

def bubble_sort(a,swaps,comps):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            comps+=1
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
                swaps+=1
    return a, swaps, comps

array=[1,14,3,12,5,10,7,8,9,6,11,4,13,2,15]
qarray=list(array)
barray=list(array)
barray,bswaps,bcomps=bubble_sort(barray,0,0)
print("Worst Case Quicksort Array:",array)
print("Quicksort - Sorted:",quicksort(qarray),"comparisons:",qcomps,"moves:",qmoves)
print("Bubble - Sorted:",barray,"comparisons:",bcomps,"swaps:",bswaps)
