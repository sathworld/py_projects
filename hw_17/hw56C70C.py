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

swap_bubble=0
swap_selection=0

comp_bubble=0
comp_selection=0

a_copy,swap_bubble,comp_bubble=bubble_sort(a_copy,swap_bubble,comp_bubble)
b_copy,swap_bubble,comp_bubble=bubble_sort(b_copy,swap_bubble,comp_bubble)
c_copy,swap_bubble,comp_bubble=bubble_sort(c_copy,swap_bubble,comp_bubble)
d_copy,swap_bubble,comp_bubble=bubble_sort(d_copy,swap_bubble,comp_bubble)

avg_swap_bubble=swap_bubble/4
avg_comp_bubble=comp_bubble/4

print("Bubble sort - average swaps:",avg_swap_bubble,"average comparisons [equal to n*(n-1)/2 for bubble sort]",avg_comp_bubble)

a,swap_selection,comp_selection=selection_sort(a,swap_selection,comp_selection)
b,swap_selection,comp_selection=selection_sort(b,swap_selection,comp_selection)
c,swap_selection,comp_selection=selection_sort(c,swap_selection,comp_selection)
d,swap_selection,comp_selection=selection_sort(d,swap_selection,comp_selection)

avg_swap_selection=swap_selection/4
avg_comp_selection=comp_selection/4

print("Selection sort - average swaps:",avg_swap_selection,"average comparisons [equal to n*(n-1)/2 for selection sort]",avg_comp_selection)
