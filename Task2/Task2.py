from math import sqrt
import sys

f = open(sys.argv[1], "r")
x = f.readline().split()
y = f.readline().split()
f.close()

# координаты центра окружности
x1 = float(x[0])
y1 = float(x[1])

# радиус
rc = float(y[0])

z = open(sys.argv[2], "r")

for line in z:
    m = line.split()
    # координаты точки
    x2 = float(m[0])
    y2 = float(m[1])
    # вычисляем длину отрезка от центра окружности до точки
    length = sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # определяем принадлежность точки
    if(length>rc):
        print(2)
    elif(length==rc):
        print(0)
    elif(length<rc):
        print(1)
z.close()