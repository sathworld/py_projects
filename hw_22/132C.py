# 132C
import numpy


def spiralMatrix(max_y, max_x, arr):
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
                arr[top][i] = counter
                counter += 1
            top += 1
            direction = 1

        elif direction == 1:
            for i in range(top, bottom + 1):
                arr[i][right] = counter
                counter += 1
            right -= 1
            direction = 2

        elif direction == 2:
            for i in range(right, left - 1, -1):
                arr[bottom][i] = counter
                counter += 1
            bottom -= 1
            direction = 3

        elif direction == 3:
            for i in range(bottom, top - 1, -1):
                arr[i][left] = counter
                counter += 1
            left += 1
            direction = 0
    return arr


def snakeMatrixDiagonal(max_y, max_x, arr):
    direction = 0
    counter = 1
    max_count = max_x * max_y
    x = 0
    y = 0
    while counter <= max_count:
        if direction == 0:
            while x >= 0 and y < max_y:
                arr[y][x] = counter
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
                arr[y][x] = counter
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
    return arr


def snakeMatrixUpDown(max_y, max_x, arr):
    left = 0
    direction = 0
    counter = 1
    while left < max_x:
        if direction == 0:
            for i in range(0, max_y):
                arr[i][left] = counter
                counter += 1
            left += 1
            direction = 1
        elif direction == 1:
            for j in range(max_y - 1, -1, -1):
                arr[j][left] = counter
                counter += 1
            left += 1
            direction = 0
    return arr


n = int(input("Enter N: "))
m = int(input("Enter M: "))

a = numpy.zeros((n, m), dtype=numpy.int16)
a = spiralMatrix(n, m, a)
print("Spiral Matrix:")
print(a)

b = numpy.zeros((n, m), dtype=numpy.int16)
b = snakeMatrixDiagonal(n, m, b)
print("Snake Matrix Diagonal:")
print(b)

c = numpy.zeros((n, m), dtype=numpy.int16)
c = snakeMatrixUpDown(n, m, c)
print("Snake Matrix UpDown:")
print(c)
