#79C
n = int(input("Enter N: \n"))
for i in range(1, n + 1):
    if (i * i)%(10 ** len(str(i))) == i:
        print(i, "*", i, "=", i * i, sep = "")
#86C
n = int(input("Enter N: \n"))
for i in range(1, n + 1):
    f = True
    s = set(list(map(int,list(str(i)))))
    try:
        for j in s:
            if i % j != 0:
                f = False
    except ZeroDivisionError:
        f = False
    if f:
        print(i, end = " ")
print()
#!!!97C
roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
arabic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
def toRoman(n):
    rom = ""
    i = 0
    while n > 0:
        for x in range(n//arabic[i]):
            rom+=roman[i]
            n-=arabic[i]
        i += 1
    print(rom)
toRoman(int(input("Enter N: \n")))

#103C
print(int(str(int(input("Enter N: \n")))[::-1]))
#106C
def GCDandLCM(a, b):
    a_orig = a
    b_orig = b
    while b != 0:
        if a > b:
            a -= b
        else:
            b -= a
    gcd = a
    try:
        lcm = int(abs(a_orig * b_orig) / gcd)
    except ZeroDivisionError:
        lcm = "Undefined"
    return gcd, lcm

a, b = list(map(int,input("Enter 2 Natural Numbers: \n").split(" ")))
gcd, lcm = GCDandLCM(a, b)
print("GCD(", a, ",", b, ")=", gcd, sep="")
print("LCM(", a, ",", b, ")=", lcm, sep="")
