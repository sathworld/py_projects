from random import randint

def printMatrix(mtx):
    for row in mtx:
        for x in row:
            print("{:4d}".format(x), end="")
        print()

size = int(input("Size:"))
mtx = [[randint(10, 99) for _ in range(size)] for _ in range(size)]

printMatrix(mtx)
print()

for i in range(size):
    for j in range(size):
        if (j - i) > 0:
            mtx[i][j] = 0

printMatrix(mtx)
