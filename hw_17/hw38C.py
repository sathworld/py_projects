import random
#38C
l = int(input("Enter the random list's length:\n"))
a=[]
c=0
for i in range(l):
    a.append(random.randint(-100,100))
print("Random list:")
print(*a)
a.sort(reverse=True)
zeros=a.count(0)
for i in range(zeros):
    a.remove(0)
    a.append(0)
print("Sorted random list:")
print(*a)
for i in range(len(a)):
    if a[i] > 0:
        c+=1
print("Count of positive numbers:",c)