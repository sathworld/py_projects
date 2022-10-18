#56B
a = list(map(int,input("Enter the list:\n").split(" ")))
a.sort()
print("Sorted list:")
print(*a)
print("Unique numbers:")
print(len(set(a)))
#56C #70C
import random
def selection_sort(a,swaps,comps):
    for i in range(len(a)):
        min_index = i
        for j in range(i+1, len(a)):
            comps+=1
            if a[min_index] > a[j]:
                min_index = j
        if (a[i] != a[min_index]):
            a[i], a[min_index] = a[min_index], a[i]
            swaps+=1
    return a, swaps, comps

def bubble_sort(a,swaps,comps):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            comps+=1
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
                swaps+=1
    return a, swaps, comps

n=1000

a=[]
b=[]
c=[]
d=[]
sink=[]
for i in range(n):
    a.append(random.randint(-100,100))
    b.append(random.randint(0,100))
    c.append(random.randint(-150,150))
    d.append(random.randint(0,10))
a_copy=list(a)
b_copy=list(b)
c_copy=list(c)
d_copy=list(d)

swap_counter_bubble=0
swap_counter_selection=0

comp_counter_bubble=0
comp_counter_selection=0

a_copy,swap_counter_bubble,comp_counter_bubble=bubble_sort(a_copy,swap_counter_bubble,comp_counter_bubble)
b_copy,swap_counter_bubble,comp_counter_bubble=bubble_sort(b_copy,swap_counter_bubble,comp_counter_bubble)
c_copy,swap_counter_bubble,comp_counter_bubble=bubble_sort(c_copy,swap_counter_bubble,comp_counter_bubble)
d_copy,swap_counter_bubble,comp_counter_bubble=bubble_sort(d_copy,swap_counter_bubble,comp_counter_bubble)

avg_swap_bubble=swap_counter_bubble/4
avg_comp_bubble=comp_counter_bubble/4

print("Bubble sort - average swaps:",avg_swap_bubble,"average comparisons [equal to n*(n-1)/2 for bubble sort]",avg_comp_bubble)

a,swap_counter_selection,comp_counter_selection=selection_sort(a,swap_counter_selection,comp_counter_selection)
b,swap_counter_selection,comp_counter_selection=selection_sort(b,swap_counter_selection,comp_counter_selection)
c,swap_counter_selection,comp_counter_selection=selection_sort(c,swap_counter_selection,comp_counter_selection)
d,swap_counter_selection,comp_counter_selection=selection_sort(d,swap_counter_selection,comp_counter_selection)

avg_swap_selection=swap_counter_selection/4
avg_comp_selection=comp_counter_selection/4

print("Selection sort - average swaps:",avg_swap_selection,"average comparisons [equal to n*(n-1)/2 for selection sort]",avg_comp_selection)

#70D
qcomps=0
qmoves=0
def quicksort(a):
    global qcomps
    global qmoves
    less = []
    equal = []
    greater = []
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

#78C
a=list(map(int,input("Enter the array:\n").split(" ")))
a.sort()
print("Sorted array: ",end="")
print(*a)
x=int(input("Enter x:\n"))
def closest(i):
    return abs(x-i)
if(min(a, key=closest)==x):
    print("Found x:",x)
else:
    print("X not found. Closest one is",min(a, key=closest))
