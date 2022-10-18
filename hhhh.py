n = int(input())
for i in range(1, n):
    zeroNotPresent = True
    divisibleByDigits = 0
    for j in str(i):
        a = int(j)
        if a == 0:
            zeroNotPresent = False
        if a != 0 and a != 1 and i % a:
            break
        else:
            divisibleByDigits = False
    else:
        print (i)
