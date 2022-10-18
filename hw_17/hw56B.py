#56B
a = list(map(int,input("Enter the list:\n").split(" ")))
a.sort()
print("Sorted list:")
print(*a)
print("Unique numbers:")
print(len(set(a)))
