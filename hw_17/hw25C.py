import random
#25C
l = int(input("Enter the random list's length:\n"))
maxn = int(input("Enter the random list's max number:\n"))
minn = int(input("Enter the random list's min number:\n"))
a = []
for i in range(l):
    a.append(random.randint(minn,maxn))
print("Random list:")
print(*a)
b = set(a)
c=[]
for i in b:
    if a.count(i) > 1:
        c.append(i)
if len(c) > 0:
    print("Repeats are: ",end="")
    print(*c)
else:
    print("No repeats")