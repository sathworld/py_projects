import random
import math
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
