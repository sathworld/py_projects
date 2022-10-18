# 132C
def printMatrix ( mtx ):
  for row in mtx:
    for x in row:
      print ( "{:4d}".format(x), end = "" )
    print ()

def spiralMatrix(max_y, max_x, mtx):
    top = 0
    bottom = max_y - 1
    left = 0
    right = max_x - 1

    direction = 0
    counter = 1
    max_count = max_x * max_y
    while counter <= max_count:
        if direction == 0:
            for i in range(left, right + 1):
                mtx[top][i] = counter
                counter += 1
            top += 1
            direction = 1

        elif direction == 1:
            for i in range(top, bottom + 1):
                mtx[i][right] = counter
                counter += 1
            right -= 1
            direction = 2

        elif direction == 2:
            for i in range(right, left - 1, -1):
                mtx[bottom][i] = counter
                counter += 1
            bottom -= 1
            direction = 3

        elif direction == 3:
            for i in range(bottom, top - 1, -1):
                mtx[i][left] = counter
                counter += 1
            left += 1
            direction = 0
    return mtx


def snakeMatrixDiagonal(max_y, max_x, mtx):
    direction = 0
    counter = 1
    max_count = max_x * max_y
    x = 0
    y = 0
    while counter <= max_count:
        if direction == 0:
            while x >= 0 and y < max_y:
                mtx[y][x] = counter
                counter += 1
                x -= 1
                y += 1
            if y == max_y:
                direction = 1
                x += 2
                y = max_y - 1
            elif x < 0:
                direction = 1
                x += 1

        elif direction == 1:
            while x < max_x and y >= 0:
                mtx[y][x] = counter
                counter += 1
                x += 1
                y -= 1
            if x == max_x:
                direction = 0
                y += 2
                x = max_x - 1
            elif y < 0:
                direction = 0
                y = 0
    return mtx


def snakeMatrixUpDown(max_y, max_x, mtx):
    left = 0
    direction = 0
    counter = 1
    while left < max_x:
        if direction == 0:
            for i in range(0, max_y):
                mtx[i][left] = counter
                counter += 1
            left += 1
            direction = 1
        elif direction == 1:
            for j in range(max_y - 1, -1, -1):
                mtx[j][left] = counter
                counter += 1
            left += 1
            direction = 0
    return mtx


n = int(input("Enter N: "))
m = int(input("Enter M: "))

a=[[None for _ in range(m)] for _ in range(n)]
b=list(a)
c=list(a)


a = spiralMatrix(n, m, a)
print("Spiral Matrix:")
printMatrix(a)


b = snakeMatrixDiagonal(n, m, b)
print("Snake Matrix Diagonal:")
printMatrix(b)


c = snakeMatrixUpDown(n, m, c)
print("Snake Matrix UpDown:")
printMatrix(c)

