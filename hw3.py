import random
import math
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
#30C
a = list(map(int,input("Enter the list:\n").split(" ")))
print("Max: ",max(a))
print("Count max:",a.count(max(a)))
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
#42C
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return (s*s == x)
def isFibonacci(n):
    return (isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4))
l = int(input("Enter the random list's length:\n"))
maxn = int(input("Enter the random list's max number:\n"))
minn = int(input("Enter the random list's min number:\n"))
a = []
b = []
for i in range(l):
    a.append(random.randint(minn,maxn))
print("Random list A:")
print(*a)
for i in a:
    if ((isFibonacci(i))and(i>=0)):
        b.append(i)
b=list(set(b))
b.sort()
print("Random list B:")
print(*b)
