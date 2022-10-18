#78C
a=list(map(int,input("Enter the array:\n").split(" ")))
a.sort()
print("Sorted array: ",end="")
print(*a)
x=int(input("Enter x:\n"))
def closest(i):
    return abs(x-i)
closest_n = min(a, key=closest)
if closest_n==x:
    print("Found x:",x)
else:
    print("X not found. Closest one is",closest_n)
