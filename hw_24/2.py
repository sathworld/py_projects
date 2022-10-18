from random import randint

def printMatrix(mtx):
    for row in mtx:
        for x in row:
            print("{:4d}".format(x), end="")
        print()

size=int(input("Size: "))
mtx = [[randint(10, 99) for _ in range(size)] for _ in range(size)]

maxn = max([max(_) for _ in mtx])
minn = min([min(_) for _ in mtx])

printMatrix(mtx)

for i in range(size):
    for j in range(size):
        if mtx[i][j] == maxn:
            print("Max A[",(i + 1),"][",(j + 1),"]=",maxn)
        if mtx[i][j] == minn:
            print("Min A[",(i + 1),"][",(j + 1),"]=",minn)
